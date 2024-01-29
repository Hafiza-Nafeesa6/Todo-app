from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    todo = models.BooleanField(default=False)
    inprogress = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media')
    link = models.URLField(blank=True)
    overdue = models.BooleanField(default=False)

    def __str__(self):
        return self.title
