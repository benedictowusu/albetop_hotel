# Generated by Django 5.0.2 on 2024-05-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_remove_standard_pictures_remove_suite_pictures_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='suite',
            name='numofSuites',
            field=models.IntegerField(default=0),
        ),
    ]
