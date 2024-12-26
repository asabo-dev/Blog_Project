from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    """Post model"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """"Return title"""
        return self.title
