# Generated by Django 4.2.6 on 2023-11-20 02:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0007_card_id_aleatorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='id_aleatorio',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]