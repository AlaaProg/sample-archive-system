from django.db import models

# Create your models here.
class Category(models.Model):
    """Category Model"""
    name = models.CharField(max_length=255, unique=True)
    note = models.TextField()

    def __str__(self):
        return self.name
