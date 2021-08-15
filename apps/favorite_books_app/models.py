from django.db import models
from datetime import date, datetime
import re
from apps.login_app.models import User


class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 1:
            errors["title"] = "Title is required"
        if len(postData['description']) < 5:
            errors["last_name"] = "Description should be at least 5 characters"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    uploaded_by  = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __repr__(self):
        return f"Book object: {self.title} ({self.id})"

