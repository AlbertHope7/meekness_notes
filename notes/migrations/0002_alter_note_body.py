# Generated by Django 4.1.7 on 2023-03-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="body",
            field=models.TextField(),
        ),
    ]
