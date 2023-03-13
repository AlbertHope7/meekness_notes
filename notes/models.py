from django.conf import settings
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notes_image = models.ImageField(upload_to="notes/", blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
