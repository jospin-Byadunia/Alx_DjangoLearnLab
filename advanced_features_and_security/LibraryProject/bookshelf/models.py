from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager  

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.IntegerField()
    class Meta:
        permissions = [
            ("can_view", "Can view"),
            ("can_create", "Can create"),
            ("can_edit", "Can edit"),
            ("can_delete", "Can delete"),
        ]

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    def __str__(self):
        return self.username


##Create User Manager for Custom User Model
# Implement a custom user manager that handles user creation and queries, ensuring it can manage the added fields effectively.

# Custom Manager Functions to Implement:
# create_user: Ensure it handles the new fields correctly.
# create_superuser: Ensure administrative users can still be created with the required fields.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user