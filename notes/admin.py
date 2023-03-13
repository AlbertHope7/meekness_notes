from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "notes_image", "body", "created_at"]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["-created_at"]
    raw_id_fields = ["author"]
