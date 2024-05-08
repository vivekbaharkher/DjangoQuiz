from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    is_correct = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.text} - {self.question.text} '
    
class Profile(models.Model):
    score=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    played=models.BooleanField(default=True)