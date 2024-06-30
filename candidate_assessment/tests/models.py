from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class AnswerChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=2)  # 'A' или 'Б'

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswerChoice, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.question} - {self.answer}'
