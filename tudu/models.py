from django.db import models

# Create your models here.


class Tudus(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)