from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

def list(request):
    categories = Category.objects.all()
    
    category_posts = {}
    for category in categories:
        posts = category.posts.order_by('-created_at')[:4]
        category_posts[category] = posts
       
    return  render(request, 'post/list.html', {'category_posts': category_posts, 'categories' : categories})

@login_required
def create(request, slug): 
    categories = Category.objects.all()
    # url에서 전돨된 slug를 이용해 특정 카테고리 가져옴
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by('-id')

    if request.method == "POST":     
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity')
        author = request.user

        if anonymity == "on": #input결과가 on으로 오나 봄
         anonymity = True
        else:
         anonymity = False
        
        post = Post.objects.create(
            title = title,
            content = content,
            anonymity = anonymity,
            author = request.user,
        )

        post.category.add(category)

        return redirect('post:list')
    return render(request, 'post/create.html', {'categories' : categories, 'category' : category, 'posts' : posts})

def detail(request, id):
    post = get_object_or_404(Post, id = id)

    return render(request, 'post/detail.html', {'post' : post})

@login_required
def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post:detail', id)
    return render(request, 'post/update.html', {'post' : post})

@login_required
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('post:list')

def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":

        anonymity = request.POST.get('anonymity')

        if anonymity == "on": 
         anonymity = True
        else:
         anonymity = False

        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            anonymity = anonymity,
            post = post,
        )
        return redirect('post:detail', post_id)