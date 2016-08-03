from django.shortcuts import render
from .models import Post, Category

# Create your views here.
def home(request):
    p = Post.objects.all().order_by('-id')
    c = Category.objects.all()
    context_dict = {'post': p, 'cat': c}
    return render(request, 'home.html', context_dict)

def blog(request, cat, slug):
    post = Post.objects.get(slug=slug)
    context_dict = {'post': post}
    return render(request, 'post.html', context_dict)
