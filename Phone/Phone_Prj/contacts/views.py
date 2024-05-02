from django.shortcuts import render, redirect, get_object_or_404
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

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        post = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email,
        )
        return redirect('contacts:list')
    return render(request, 'contacts/create.html')

def detail(request, id):
    post = get_object_or_404(Phone, id = id)

    return render(request, 'contacts/detail.html', {'post' : post})

def update(request, id):
    post = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        post.name = request.POST.get('name')
        post.phone_num = request.POST.get('phone_num')
        post.email = request.POST.get('email')
        post.save()
        return redirect('contacts:list')
    return render(request, 'contacts/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        post.delete()
        return redirect('contacts:list')
    return render(request, 'contacts/delete.html', {'post' : post})

"""
FBV 방식
def list(request):
    posts = Phone.objects.all().order_by('name')
    return render(request, "contacts/list.html", {'posts' : posts})
"""
