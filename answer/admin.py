from django.contrib import admin
from .models import answer


class answerAdmin(admin.ModelAdmin):
    list_display=['question', 'upvote', 'downvote', 'date']
    search_fields=['question']

admin.site.register(answer, answerAdmin)
