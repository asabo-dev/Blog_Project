from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text