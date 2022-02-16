from django.contrib import admin,messages
from .models import questionCategory,question

def inactive_status(self, request, queryset):
    queryset.update(status=False)
    messages.success(request, 'All selected status marked as inactive')
def active_status(self, request, queryset):
    queryset.update(status=True)
    messages.success(request, 'All selected status marked as active')

class questionCategoryadmin(admin.ModelAdmin):
    list_display=['name', 'status']
    list_filter=['status']
    search_fields=['name']
    actions=[active_status, inactive_status]


admin.site.register(questionCategory, questionCategoryadmin)

class questionAdmin(admin.ModelAdmin):
    list_display=['question','upvote', 'downvote','date', 'author','category']
    search_fields=['question','category']

admin.site.register(question, questionAdmin)