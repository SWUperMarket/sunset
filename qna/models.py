from django.db import models
from common.models import User

# Create your models here.
"""
 * MODEL No. 1
 * MODEL Name : Question
"""
class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

"""
 * MODEL No. 2
 * MODEL Name : Answer
"""
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()