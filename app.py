import os
import io
import json
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, send_file, abort, jsonify, Response
from flask_pymongo import PyMongo
from bson import ObjectId
import gridfs
from pdfminer.high_level import extract_text

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/book_shelf")
app.secret_key = os.getenv("FLASK_SECRET", "dev-secret")

mongo = PyMongo(app)
# Get the actual PyMongo Database object
db = mongo.cx.get_database("book")  
fs = gridfs.GridFS(db)



# ---------- Utility: very small "AI" emotion classifier -----------
# Rule-based keywords -> emotion; fallback to sentiment-ish neutral.
EMOTION_LEX = {
    "joy": {"happy","joy","delight","smile","cheer","excited","love","thrill","glad"},
    "sad": {"sad","cry","tears","sorrow","pain","lonely","mourn","regret","gloom"},
    "anger": {"angry","rage","furious","annoy","irritate","hate","wrath","resent"},
    "fear": {"fear","scare","afraid","terror","panic","worry","anxious","dread"},
}

def classify_sentence_emotion(s):
    w = {word.strip(".,!?;:()[]\"'").lower() for word in s.split()}
    scores = {e: len(w & lex) for e, lex in EMOTION_LEX.items()}
    # prefer non-zero; otherwise neutral
    best = max(scores.items(), key=lambda kv: kv[1])
    if best[1] == 0:
        # tiny heuristic: exclamation -> joy/anger; question -> fear/neutral
        if "!" in s:
            return "joy"
        if "?" in s:
            return "fear"
        return "neutral"
    return best[0]


# --------------------------- Routes -------------------------------

@app.route("/")
def home():
    # List minimal metadata for shelf
    books = list(db.books.find({}, {"title":1,"author":1,"cover_id":1,"created_at":1}))
    # newest first
    books.sort(key=lambda b: b.get("created_at", datetime.min), reverse=True)
    # attach URLs
    for b in books:
        b["_id"] = str(b["_id"])
        if b.get("cover_id"):
            b["cover_url"] = url_for("cover_file", file_id=str(b["cover_id"]))
        else:
            b["cover_url"] = url_for("static", filename="img/default-cover.png")
    return render_template("index.html", books=books)


@app.route("/admin")
def admin_page():
    books = []
    for b in db.books.find().sort("created_at", -1):
        b["_id"] = str(b["_id"])  # make it a plain string
        if "cover_id" in b and b["cover_id"]:
            b["cover_id"] = str(b["cover_id"])
        books.append(b)
    return render_template("admin.html", books=books)





@app.route("/admin/upload", methods=["POST"])
def admin_upload():
    title = request.form.get("title", "").strip() or "Untitled"
    author = request.form.get("author", "").strip() or "Unknown"
    description = request.form.get("description", "").strip()
    tags = [t.strip() for t in request.form.get("tags","").split(",") if t.strip()]

    file = request.files.get("file")
    cover = request.files.get("cover")
    if not file:
        return "No file provided", 400

    filename = file.filename
    content = file.read()
    file.seek(0)

    # Store main file in GridFS
    mimetype = file.mimetype or "application/pdf"
    file_id = fs.put(content, filename=filename, contentType=mimetype)

    cover_id = None
    if cover and cover.filename:
        cover_id = fs.put(cover.read(), filename=cover.filename, contentType=cover.mimetype)

    doc = {
        "title": title,
        "author": author,
        "description": description,
        "tags": tags,
        "file_id": file_id,
        "cover_id": cover_id,
        "filename": filename,
        "mimetype": file.mimetype,
        "created_at": datetime.utcnow()
    }
    inserted = db.books.insert_one(doc)
    return redirect(url_for("home"))


from bson import ObjectId
from flask import flash, redirect, url_for

@app.route("/admin/delete/<book_id>", methods=["POST"])
def admin_delete(book_id):
    try:
        book = db.books.find_one({"_id": ObjectId(book_id)})
        if not book:
            flash("Book not found.", "error")
            return redirect(url_for("admin_page"))

        # Delete cover file if exists
        if book.get("cover_id"):
            try:
                fs.delete(ObjectId(book["cover_id"]))
            except Exception:
                pass  # Ignore if file not found

        # Delete the book document
        db.books.delete_one({"_id": ObjectId(book_id)})

        flash("Book deleted successfully!", "success")
    except Exception as e:
        flash(f"Error deleting book: {e}", "error")

    return redirect(url_for("admin_page"))


from bson import ObjectId
from flask import Response

@app.route("/cover/<book_id>")
def get_cover(book_id):
    book = db.books.find_one({"_id": ObjectId(book_id)})
    if book and book.get("cover_id"):
        cover_data = fs.get(book["cover_id"]).read()
        return Response(cover_data, mimetype="image/jpeg")  # Change mimetype if needed
    return "", 404





@app.route("/book/<book_id>")
def book_view(book_id):
    book = db.books.find_one({"_id": ObjectId(book_id)})
    if not book:
        abort(404)
    book["_id"] = str(book["_id"])
    cover_url = url_for("cover_file", file_id=str(book["cover_id"])) if book.get("cover_id") else url_for("static", filename="img/default-cover.png")
    return render_template("reader.html", book=book, cover_url=cover_url)


@app.route("/book/<book_id>/file")
def book_file(book_id):
    book = db.books.find_one({"_id": ObjectId(book_id)})
    if not book:
        abort(404)
    gf = fs.get(book["file_id"])
    return send_file(io.BytesIO(gf.read()), mimetype=gf.content_type or "application/octet-stream", as_attachment=False, download_name=gf.filename)


@app.route("/file/<file_id>/cover")
def cover_file(file_id):
    try:
        gf = fs.get(ObjectId(file_id))
    except:
        abort(404)
    return send_file(io.BytesIO(gf.read()), mimetype=gf.content_type or "image/jpeg", as_attachment=False, download_name=gf.filename)


@app.route("/api/books")
def api_books():
    """Return books for shelf (if you want client-side fetch)."""
    books = list(db.books.find({}, {"title":1,"author":1,"cover_id":1,"created_at":1}))
    books.sort(key=lambda b: b.get("created_at", datetime.min), reverse=True)
    out = []
    for b in books:
        out.append({
            "id": str(b["_id"]),
            "title": b.get("title","Untitled"),
            "author": b.get("author","Unknown"),
            "cover": url_for("cover_file", file_id=str(b["cover_id"])) if b.get("cover_id") else url_for("static", filename="img/default-cover.png")
        })
    return jsonify(out)


@app.route("/api/analyze_emotions", methods=["POST"])
def analyze_emotions():
    """
    Accepts: { "text": "full text chunk" }
    Returns: [{ "sentence": "...", "emotion": "joy|sad|anger|fear|neutral" }, ...]
    """
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"error": "No text"}), 400

    # naive sentence split
    import re
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    results = [{"sentence": s, "emotion": classify_sentence_emotion(s)} for s in sentences]
    return jsonify(results)


@app.route("/api/extract_text/<book_id>", methods=["GET"])
def extract_pdf_text(book_id):
    """
    Extract plain text (first N chars) from PDFs for TTS.
    For non-PDFs, returns empty string.
    """
    MAX_CHARS = 6000  # keep payload reasonable
    book = db.books.find_one({"_id": ObjectId(book_id)})
    if not book:
        return jsonify({"text": ""})
    gf = fs.get(book["file_id"])
    if (gf.content_type or "").lower().startswith("application/pdf") or (book.get("filename","").lower().endswith(".pdf")):
        data = gf.read()
        try:
            text = extract_text(io.BytesIO(data)) or ""
            return jsonify({"text": text[:MAX_CHARS]})
        except Exception:
            return jsonify({"text": ""})
    return jsonify({"text": ""})


if __name__ == "__main__":
    app.run(debug=True)
