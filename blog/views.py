from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    p = Post.objects.all()
    context_dict = {'post': p}
    return render(request, 'home.html', context_dict)
