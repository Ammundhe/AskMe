from django.db import models
from django.contrib.auth.models import User

class userprofile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.TextField()
    mobile=models.CharField(max_length=10)
    profile_picture=models.ImageField()
    
    def __str__(self) -> str:
        return str(self.user)