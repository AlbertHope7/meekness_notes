# Generated by Django 4.1.7 on 2023-03-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0003_note_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="notes_image",
            field=models.ImageField(blank=True, upload_to="notes/"),
        ),
    ]
