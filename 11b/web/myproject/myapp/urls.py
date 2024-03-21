# myapp/urls.py
from django.urls import path
from .views import create_post, post_created

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('post-created/', post_created, name='post_created'),  # Define the post_created URL pattern
    # Define more URLs if needed
]