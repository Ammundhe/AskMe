from django.db import models
from question.models import question
from django.contrib.auth.models import User


class answer(models.Model):
    question=models.ForeignKey(question, on_delete=models.CASCADE, related_name="answer")
    image=models.ImageField(upload_to="media", null=True, blank=True)
    answer=models.TextField()
    upvote=models.IntegerField(default=0)
    downvote=models.IntegerField(default=0)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField(null=True, blank=True)



    def __str__(self) -> str:
        return str(self.question)

