# Generated by Django 4.2.7 on 2023-11-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_endereco_postagem_user_delete_card_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='assunto',
            field=models.CharField(max_length=50, verbose_name='Assunto'),
        ),
    ]
