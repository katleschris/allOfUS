from django.db import models

# Create your models here.
class Question(models.model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

