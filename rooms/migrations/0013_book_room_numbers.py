# Generated by Django 5.0.2 on 2024-06-03 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0012_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='room_numbers',
            field=models.TextField(default=1),
        ),
    ]
