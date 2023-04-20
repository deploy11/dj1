from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.CharField(max_length=1000)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)