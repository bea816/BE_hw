from django.shortcuts import render
from .models import Phone
from django.views.generic import ListView

class IndexView(ListView):
    queryset = Phone.objects.all().order_by('name')
    template_name = "contacts/list.html"
    context_object_name = 'posts'


def result(request):
   entered_text = request.GET['data']
   posts = Phone.objects.all()

   matchings = []

   for post in posts:
      if entered_text in post.name:
        matchings.append(post)

   return render(request, "contacts/result.html", {'matchings': matchings, 'entered_text': entered_text})



"""
FBV 방식
def list(request):
    posts = Phone.objects.all().order_by('name')
    return render(request, "contacts/list.html", {'posts' : posts})
"""
