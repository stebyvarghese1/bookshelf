import os
from supabase import create_client, Client
from django.conf import settings

# Load Supabase credentials from environment
SUPABASE_URL = os.getenv("SUPABASE_URL", "<your-supabase-url>")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "<your-supabase-key>")
BUCKET_NAME = "books"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def upload_file(file_obj, file_path):
    """Upload file to Supabase Storage and return public URL"""
    # Convert Django InMemoryUploadedFile to bytes
    file_bytes = file_obj.read()
    file_obj.seek(0)  # reset pointer for later use

    supabase.storage.from_(BUCKET_NAME).upload(
        path=file_path,
        file=file_bytes,
        file_options={"content-type": file_obj.content_type, "upsert": "true"},
    )

    # Return public URL
    return supabase.storage.from_(BUCKET_NAME).get_public_url(file_path)


def delete_file(file_url):
    """Delete file from Supabase Storage using public URL"""
    try:
        # extract the path after `/object/public/books/`
        prefix = f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET_NAME}/"
        if not file_url.startswith(prefix):
            return False

        file_path = file_url.replace(prefix, "")

        supabase.storage.from_(BUCKET_NAME).remove([file_path])
        return True
    except Exception as e:
        print("❌ Delete failed:", e)
        return False
