from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=20)
    review = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
