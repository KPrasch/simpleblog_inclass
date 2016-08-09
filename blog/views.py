from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def home(request):
    p = Post.objects.all().order_by('-id')
    c = Category.objects.all()
    context_dict = {'post': p, 'cat': c}
    return render(request, 'home.html', context_dict)


def blog(request, cat, slug):
    post = Post.objects.get(slug=slug)
    context_dict = {'post': post}
    return render(request, 'post.html', context_dict)


def cat(request, cat):
    post = Post.objects.filter(category__slug=cat)
    context_dict = {'post': post}
    return render(request, 'category.html', context_dict)


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['category', 'title', 'slug', 'img', 'content']
    template_name = 'edit_post.html'
    success_url = '/'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'content', 'img']
    success_url = '/'
    template_name = 'post_new.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        form.instance.slug = slugify(form.instance.title)
        return super(CreatePost, self).form_valid(form)


class DeletePost(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'confirm_delete.html'
