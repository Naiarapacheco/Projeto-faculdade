from django.shortcuts import render

from blog.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'core/home.html', {'posts':posts})
