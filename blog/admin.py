from django.contrib import admin
from .models import blog, PostCategory

class PostCategoryAdmin(admin.ModelAdmin):
    list_dislpay=('name', 'status')
    list_filter=('status',)
    search_filter=['name',]

admin.site.register(PostCategory,PostCategoryAdmin)

class blogAdmin(admin.ModelAdmin):
    list_display=['title','author','date']
    search_fields=['title']


admin.site.register(blog)
