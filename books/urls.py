from django.urls import path
from . import views

urlpatterns = [
    # Admin / internal (management side)
    path("", views.home, name="home"),
    path("books/", views.book_list, name="book_list"),
    path("books/upload/", views.book_upload, name="book_upload"),
    path("books/edit/<int:pk>/", views.book_edit, name="book_edit"),  # ✅ Edit route
    path("books/delete/<int:pk>/", views.book_delete, name="book_delete"),

    # Public bookshelf (user-facing)
    path("bookshelf/", views.bookshelf, name="bookshelf"),

    # Reader (user-facing)
    path("books/<int:pk>/pdf/", views.serve_pdf, name="serve_pdf"),
    path("books/<int:pk>/cover/", views.serve_cover_image, name="book_cover"),
    path("books/<int:pk>/read/", views.read_book, name="read_book"),
]
