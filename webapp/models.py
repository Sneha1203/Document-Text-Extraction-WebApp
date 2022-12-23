from django.db import models
from django.contrib.auth.models import User

class Documents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    file = models.FileField(),
    file_name = models.CharField(),
    file_path = models.FilePathField(),
    text_extracted = models.TextField()