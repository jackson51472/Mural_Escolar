from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    turma = models.CharField(max_length=50, null=True)  # Defina como nulo

    def __str__(self):
        return self.title
