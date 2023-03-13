from rest_framework import serializers
from notes.models import Note


class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = [
            "id",
            "title",
            "slug",
            "author",
            "notes_image",
            "body",
            "created_at",
        ]
