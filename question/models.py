from django.db import models
from django.contrib.auth.models import User


class questionCategory(models.Model):
    name=models.CharField(max_length=255)
    status=models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.name)

class question(models.Model):
    category=models.ForeignKey(questionCategory, on_delete=models.CASCADE)
    question=models.TextField()
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)
    date=models.DateField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.question)

