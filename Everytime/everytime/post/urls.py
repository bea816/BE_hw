from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('list/', list, name = "list"),
    path('detail/<int:id>', detail, name = "detail"),
    path('update/<int:id>', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
    path('create-comment/<int:post_id>/', create_comment, name = "create-comment"),
    path('create/<slug:slug>/', create, name = "create"),
]

