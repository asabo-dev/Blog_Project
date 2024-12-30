from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    """Model representing a blog post category."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        '''Create a slug when saving a category.'''
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        '''Return the category name.'''
        return self.name

class Post(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name="posts")
    date_posted = models.DateTimeField(auto_now_add=True)
    

    def save(self, *args, **kwargs):
        """Create a slug when saving a post."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """Return the post title."""
        return self.title

class Comment(models.Model):
    """Model representing a comment on a blog post."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        """Return a string representation of the comment."""
        return f"Comment by {self.author} on {self.post.title}"

class Tag(models.Model):
    """Model representing a blog post tag."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        '''Create a slug when saving a tag.'''
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        '''Return the tag name.'''
        return self.name

class PostTag(models.Model):
    """Model representing a blog post tag relationship."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post_tags')

    def __str__(self):
        """Return a string representation of the post tag relationship."""
        return f"{self.post.title} - {self.tag.name}"

class Entry(models.Model):
    """Model representing a blog post entry."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='entries')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the entry title."""
        return self.title