from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

user = get_user_model()


class Document(models.Model):
    """Document Model"""

    title = models.CharField(max_length=255)
    note = models.TextField()
    date = models.DateField(null=False)
    add_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="documents")
    category = models.ForeignKey("category.Category", on_delete=models.CASCADE, related_name="documents")


    def __str__(self):
        return self.title
    