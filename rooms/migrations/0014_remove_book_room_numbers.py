# Generated by Django 5.0.2 on 2024-06-03 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0013_book_room_numbers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='room_numbers',
        ),
    ]
