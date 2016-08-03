from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    # list_filter = ['title', 'slug']
    # list_display = ['title', 'slug']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
