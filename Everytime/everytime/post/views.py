from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

def list(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-id')
    
    return  render(request, 'post/list.html', {'posts' : posts, 'categories' : categories})

@login_required
def create(request, slug): 
    categories = Category.objects.all()

    if request.method == "POST":
        new_post = POST()
        new_post.category = Category.objects.get(slug=slug)
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = request.POST.get('anonymity')
        author = request.user
         
        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]

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

        for category in categories:
            post.category.add(category)

        return redirect('post:list')
    return render(request, 'post/create.html', {'categories' : categories})

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