from django.db import models
from user.models import User

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f'[{self.title}]'

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    anonymity = models.BooleanField(default=True)
    author = models.ForeignKey(to = User, null=True, on_delete=models.CASCADE, related_name = "posts")
    category = models.ManyToManyField(to=Category, through="PostCategory", related_name="posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name = "comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    anonymity = models.BooleanField(default=True)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "comments")

    def __str__(self):
        return f'[{self.id}] {self.content}'

class PostCategory(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name="categories_postcategory")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="posts_postcategory")
