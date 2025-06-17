from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
# here second param is templates
def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})
# def index(request):
#     return HttpResponse('<h1 >hello</h1>')
def post(request,pk):
    posts=Post.objects.get(id=pk)
    return render(request,'post.html',{'post':posts})
