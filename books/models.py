from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password


# -------------------- USER --------------------
class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


# -------------------- BOOK --------------------
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)

    file_url       = models.URLField(max_length=500, blank=True, null=True)    # Drive PDF link
    cover_url      = models.URLField(max_length=500, blank=True, null=True)    # Drive image link
    total_pages    = models.PositiveIntegerField(default=0)

    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title



# -------------------- CUSTOM ADMIN --------------------
class AdminUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        # enforce only one AdminUser in DB
        if not self.pk and AdminUser.objects.exists():
            AdminUser.objects.all().delete()  # delete old admin(s)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
