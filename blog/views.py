from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Post, Comment

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('details', slug=slug)
        else:
            form = CommentForm()

    return render(request,'blog/detail.html', {'post': post, 'form': form})