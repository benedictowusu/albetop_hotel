# Generated by Django 5.0.2 on 2024-07-17 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0017_book_check_in_book_check_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip',
            name='numberofbedrooms',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='vip',
            name='pricepernight',
            field=models.IntegerField(default=1200),
        ),
    ]
