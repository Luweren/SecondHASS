from django.db import models


class Todo(models.Model):
    todo_text = models.TextField()
    deadline = models.DateField()
    progress = models.FloatField()
