# Generated by Django 4.2.6 on 2023-11-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_card_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]
