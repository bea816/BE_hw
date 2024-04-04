from django.shortcuts import render
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