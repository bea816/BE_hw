from django.urls import path, include
from .views import index, create, detail, update, delete

app_name = 'posts'

urlpatterns = [
    path('', index, name = "index"),
    path('create/', create, name = "create"),
    path('detail/<int:id>', detail, name = "detail"),
    path('update/<int:id>', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
]