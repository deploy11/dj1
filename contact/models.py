from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    subject = models.CharField(max_length=500)
    text = models.TextField()