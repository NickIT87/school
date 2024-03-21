# myapp/views.py
from django.shortcuts import render, redirect
from django.urls import reverse   # Import reverse

from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('post_created'))  # Redirect to a success page
    else:
        form = PostForm()
    return render(request, 'myapp/create_post.html', {'form': form})


def post_created(request):
    return render(request, 'myapp/post_created.html')  # Create a simple template for post creation success
