from django.shortcuts import render
from .models import Post
from django.db.models import Q
from django.views.generic import DetailView
# Create your views here.
def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        post = Post.objects.filter(Q(title__icontains=q))
    else:
        post = Post.objects.all()
      
    return render(request,'blog.html',{'post':post})
class detail(DetailView):
    model = Post
    template_name = 'blog-single.html'