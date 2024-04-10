from django.urls import path
from .views import *

app_name = 'contacts'

urlpatterns = [
    path('', IndexView.as_view(), name='list'),
    path('result/', result, name="result"),
]