from django.db import models
from django.contrib.auth.models import User


def post_upload_handler(instance, filename):
    return "{slug}/img/{file}".format(slug=instance.slug, file=filename)


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category)
    date_created = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User)
    img = models.ImageField(upload_to=post_upload_handler)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
