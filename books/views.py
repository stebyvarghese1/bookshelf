from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Book, AdminUser
from .forms import AdminLoginForm, AdminUpdateForm
from PyPDF2 import PdfReader
import io

# -------------------- PUBLIC PAGES --------------------
def home(request):
    return render(request, "home.html")


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


from .supabase_service import upload_file, delete_file

def book_upload(request):
    if request.method == "POST" and request.FILES.get("file"):
        pdf_file = request.FILES["file"]
        pdf_path = f"pdfs/{pdf_file.name}"
        pdf_url = upload_file(pdf_file, pdf_path)

        # count pages
        pdf_reader = PdfReader(io.BytesIO(pdf_file.read()))
        total_pages = len(pdf_reader.pages)
        pdf_file.seek(0)

        # upload optional cover
        cover_file = request.FILES.get("cover_image")
        cover_url = None
        if cover_file:
            cover_path = f"covers/{cover_file.name}"
            cover_url = upload_file(cover_file, cover_path)

        # save to DB
        book = Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
            about=request.POST.get("about"),
            file_url=pdf_url,
            cover_url=cover_url,
            total_pages=total_pages,
        )
        messages.success(request, "✅ Book uploaded successfully!")
        return redirect("book_list")

    return render(request, "books/book_upload.html")


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.about = request.POST.get("about")

        # ✅ Replace PDF
        if request.FILES.get("file"):
            # delete old file if exists
            if book.file_url:
                delete_file(book.file_url)

            new_pdf = request.FILES["file"]
            pdf_path = f"pdfs/{new_pdf.name}"
            pdf_url = upload_file(new_pdf, pdf_path)

            # count pages
            pdf_reader = PdfReader(io.BytesIO(new_pdf.read()))
            total_pages = len(pdf_reader.pages)
            new_pdf.seek(0)

            book.file_url = pdf_url
            book.total_pages = total_pages

        # ✅ Replace cover manually
        if request.FILES.get("cover_image"):
            if book.cover_url:
                delete_file(book.cover_url)

            cover_file = request.FILES["cover_image"]
            cover_path = f"covers/{cover_file.name}"
            cover_url = upload_file(cover_file, cover_path)
            book.cover_url = cover_url

        book.save()
        messages.success(request, "✅ Book updated successfully!")
        return redirect("book_list")

    return render(request, "books/book_edit.html", {"book": book})

from .supabase_service import upload_file, delete_file   # make sure this is imported

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if book.file_url:
        delete_file(book.file_url)
    if book.cover_url:
        delete_file(book.cover_url)

    book.delete()
    messages.success(request, "🗑️ Book deleted successfully!")
    return redirect("book_list")



def serve_pdf(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if not book.file_url:
        return HttpResponse("❌ No PDF found", status=404)
    return redirect(book.file_url)


def serve_cover_image(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if not book.cover_url:
        return HttpResponse("❌ No cover found", status=404)
    return redirect(book.cover_url)


def bookshelf(request):
    books = Book.objects.all()
    return render(request, "books/bookshelf.html", {"books": books})


def read_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/read_book.html", {"book": book})


# -------------------- ADMIN PAGES --------------------
def admin_login(request):
    if request.method == "POST":
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                admin_user = AdminUser.objects.get(username=username)
                if admin_user.check_password(password):
                    request.session['admin_logged_in'] = True
                    messages.success(request, "✅ Logged in successfully!")
                    return redirect("admin_home")
                else:
                    messages.error(request, "❌ Invalid password.")
            except AdminUser.DoesNotExist:
                messages.error(request, "❌ Admin user does not exist.")
    else:
        form = AdminLoginForm()
    return render(request, "books/admin_login.html", {"form": form})


def admin_home(request):
    if not request.session.get('admin_logged_in'):
        return redirect("admin_login")
    return render(request, "home.html")


def admin_logout(request):
    request.session.flush()
    messages.success(request, "✅ Logged out successfully!")
    return redirect("admin_login")


def update_credentials(request):
    if not request.session.get('admin_logged_in'):
        return redirect("admin_login")

    admin_user = AdminUser.objects.first()
    if request.method == "POST":
        form = AdminUpdateForm(request.POST)
        if form.is_valid():
            admin_user.username = form.cleaned_data["username"]
            admin_user.set_password(form.cleaned_data["password"])
            admin_user.save()
            messages.success(request, "✅ Credentials updated successfully!")
            return redirect("admin_home")
    else:
        form = AdminUpdateForm(initial={"username": admin_user.username})

    return render(request, "books/update_credentials.html", {"form": form})
