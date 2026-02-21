from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from books import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # Favicon route to prevent 404 errors
    path("favicon.ico", TemplateView.as_view(template_name="favicon.ico", content_type="image/x-icon")),
    
    # --- Custom Admin Phase ---
    path("admin/", views.admin_login, name="admin_login"),
    path("admin/home/", views.admin_home, name="admin_home"),
    path("admin/logout/", views.admin_logout, name="admin_logout"),
    path("admin/update-credentials/", views.update_credentials, name="update_credentials"),

    # --- Django Default Admin (for superuser) ---
    # path("djadmin/", admin.site.urls),  # Commented out to prevent /admin/ redirect conflicts

    # --- User / Public Phase ---
    path("", views.bookshelf, name="home"),  # Root → Bookshelf
    path("read/<int:pk>/", views.read_book, name="read_book"),

    # --- API Endpoints ---
    path("api/", include("books.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# Media & Static (for dev mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
