from django.contrib import admin
from django import forms
from .models import Book

class BookAdminForm(forms.ModelForm):
    file = forms.FileField(required=False, help_text="Upload a PDF file to Google Drive")
    cover = forms.FileField(required=False, help_text="Upload a custom cover (optional)")

    class Meta:
        model = Book
        fields = ["title", "author", "about"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = ("title", "author", "total_pages", "file_url", "cover_url")
    search_fields = ("title", "author")
    readonly_fields = ("gdrive_file_id", "file_url", "cover_url", "total_pages")


    def save_model(self, request, obj, form, change):
        pdf_file = form.cleaned_data.get("file")
        if pdf_file:
            pdf_id, pdf_url, total_pages, cover_id, cover_url = upload_pdf_and_cover(pdf_file, pdf_file.name)
            obj.gdrive_file_id = pdf_id
            obj.file_url = pdf_url
            obj.total_pages = total_pages
            obj.cover_url = cover_url

        custom_cover = form.cleaned_data.get("cover")
        if custom_cover:
            cover_id, cover_url = upload_image(custom_cover, custom_cover.name)
            obj.cover_url = cover_url

        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if obj.gdrive_file_id:
            delete_from_drive(obj.gdrive_file_id)
        if obj.cover_url:
            delete_from_drive(obj.cover_url)
        super().delete_model(request, obj)
