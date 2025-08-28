from books.models import AdminUser

# Create superuser
admin = AdminUser(username="admin")
admin.set_password("admin123")  # change this password
admin.save()
