# Generated by Django 4.2.4 on 2023-08-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='calories',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
