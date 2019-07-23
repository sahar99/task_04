from django.db import models

class Article(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    opening_time=models.DateTimeField()
    closing_time=models.DateTimeField()

    def __str__(self):
        return self.name
