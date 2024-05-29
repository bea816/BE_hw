from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', list, name = "list"),
    path('create/', create, name = "create"),
    path('detail/<int:id>', detail, name = "detail"),
    path('update/<int:id>', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
    path('create-comment/<int:post_id>/', create_comment, name = "create-comment"),
    path('add-like/<int:post_id>/', add_like, name = "add-like"),
    path('remove-like/<int:post_id>/', remove_like, name = "remove-like"),
    path('my-like/', mylike, name="my-like"),
]