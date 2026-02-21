import os
import time
from supabase import create_client, Client
from django.conf import settings
from httpx import RemoteProtocolError, ConnectError, TimeoutException

# Load Supabase credentials from environment
SUPABASE_URL = os.getenv("SUPABASE_URL", "<your-supabase-url>")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "<your-supabase-key>")
BUCKET_NAME = "books"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def upload_file(file_obj, file_path):
    """Upload file to Supabase Storage with retry logic"""
    # Convert Django InMemoryUploadedFile to bytes
    file_bytes = file_obj.read()
    file_obj.seek(0)  # reset pointer for later use
    
    last_error = None
    
    for attempt in range(MAX_RETRIES):
        try:
            supabase.storage.from_(BUCKET_NAME).upload(
                path=file_path,
                file=file_bytes,
                file_options={"content-type": file_obj.content_type, "upsert": "true"},
            )
            
            # Return public URL on success
            return supabase.storage.from_(BUCKET_NAME).get_public_url(file_path)
            
        except (RemoteProtocolError, ConnectError, TimeoutException) as e:
            last_error = e
            if attempt < MAX_RETRIES - 1:
                wait_time = RETRY_DELAY * (2 ** attempt)  # exponential backoff
                print(f"⚠️ Upload attempt {attempt + 1} failed, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"❌ Upload failed after {MAX_RETRIES} attempts")
        except Exception as e:
            # For other errors, raise immediately
            print(f"❌ Upload error: {e}")
            raise
    
    # If we exhausted retries, raise the last error
    raise Exception(f"Failed to upload file after {MAX_RETRIES} attempts: {last_error}")


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
