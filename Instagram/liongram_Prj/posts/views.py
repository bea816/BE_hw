from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.db.models import Q

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "posts/index.html", {'posts' : posts})
    #posts 안 쓰니까 TemplateDoesNotExist에러 발생

def result(request):
    entered_text = request.GET['data']
    posts = Post.objects.filter(Q(title__contains = entered_text) | Q(content__contains = entered_text))

    return render(request, "posts/result.html", {'posts': posts, 'entered_text': entered_text})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        post = Post.objects.create(
            title = title,
            content = content,
        )
        return redirect('posts:index')
    return render(request, 'posts/create.html')

def detail(request, id):
    post = get_object_or_404(Post, id = id)
    
    views = Post.objects.get(pk=id)
    views.increase_views()

    return render(request, 'posts/detail.html', {'post' : post, 'views' : views})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', id)
    return render(request, 'posts/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('posts:index')