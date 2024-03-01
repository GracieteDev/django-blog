from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"
#This means that we can now leave some posts in Draft while we finish them, and they will not show up on the live blog.