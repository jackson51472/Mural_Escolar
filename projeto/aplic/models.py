import uuid
from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    turma = models.CharField(max_length=50, null=True)
    data = models.DateField(null=True)
    hora = models.TimeField(null=True)
    id_aleatorio = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title
    
for card in Card.objects.all():
    card.id_aleatorio = uuid.uuid4()
    card.save()

