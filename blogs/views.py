from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    """The home page for Blogs."""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all posts."""
    posts = Post.objects.order_by('date_posted')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    """Show a single post and all its comments."""
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by('-date_posted')
    context = {'post': post, 'comments': comments}
    return render(request, 'blogs/post.html', context)