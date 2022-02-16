from django.db import models
from django.contrib.auth.models import User

class PostCategory(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)

class blog(models.Model):
    category=models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    slug=models.SlugField()
    cover_image=models.ImageField()
    description=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField()
    
    def __str__(self) -> str:
        return str(self.title)