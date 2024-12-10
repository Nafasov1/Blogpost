from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Article

class BlogView(TemplateView):

    template_name = 'blog/blog.html'




