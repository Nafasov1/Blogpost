from django.urls import path

from .views import BlogView

app_name = 'blog_app'


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
]

