from django.contrib import admin
from .models import userprofile

class userprofileAdmin(admin.ModelAdmin):
    list_display=['user','mobile']
    search_fields=['user']


admin.site.register(userprofile, userprofileAdmin)
