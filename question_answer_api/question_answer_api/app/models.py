from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    question = models.CharField(max_length=243)
    answer = models.CharField(max_length=243)
    date = models.DateTimeField(auto_now_add=True)

    