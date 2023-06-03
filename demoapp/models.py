from django.db import models

# Create your models here.
from datetime import datetime


class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    description=models.TextField()
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now)
    def_str_(self):
        return self.title