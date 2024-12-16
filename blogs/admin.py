from django.contrib import admin

from .models import Topic, Entry

# Register your models here.
from .models import Blog, Blogpost

admin.site.register(Blog)
admin.site.register(Blogpost)
