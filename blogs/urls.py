"""Defines URL patterns for Blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all posts
    path('posts/', views.posts, name='posts'),
    # Detail page for a single post
    path('posts/<int:post_id>/', views.post, name='post'),
    # Page for adding a new post
    path('new_post/', views.new_post, name='new_post'),
]