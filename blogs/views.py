from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    """The home page for Blogs."""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all posts."""
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)