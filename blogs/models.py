from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    #image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class Blogpost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    #image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title