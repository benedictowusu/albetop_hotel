# Generated by Django 5.0.2 on 2024-05-05 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_alter_standard_pricepernight_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standard',
            name='pictures',
        ),
        migrations.RemoveField(
            model_name='suite',
            name='pictures',
        ),
        migrations.RemoveField(
            model_name='vip',
            name='pictures',
        ),
    ]
