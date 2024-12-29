from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm

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
    """Show a single post and its comments."""
    post = Post.objects.get(id=post_id)
    comments = post.comments.filter(approved=True)
    context = {'post': post, 'comments': comments}
    return render(request, 'blogs/post.html', context)

def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PostForm()
    else:
        # POST data submitted; process data.
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save()
            return redirect('blogs:posts')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def new_comment(request, post_id):
    """Add a new comment."""
    post = Post.objects.get(id=post_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = CommentForm()
    else:
        # POST data submitted; process data.
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('blogs:post', post_id=post_id)
    # Display a blank or invalid form.
    context = {'post': post, 'form': form}
    return render(request, 'blogs/new_comment.html', context)