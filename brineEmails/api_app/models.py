from django.db import models

# Create your models here.
class EmailItem(models.Model):
    email = models.EmailField(max_length = 200)