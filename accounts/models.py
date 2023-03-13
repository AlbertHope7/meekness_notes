from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150)
    date_of_birth = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.email
