from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import *

def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()

    return redirect('post_detail', category_slug=comment.post.category.slug, slug=comment.post.slug)

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug, category_slug=category_slug)
        else:
            form = CommentForm()

    return render(request,'blog/detail.html', {'post': post, 'form': form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts':posts})

def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query)) #icontains -> is insensitive to lowercase and capital letters.
    
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})

