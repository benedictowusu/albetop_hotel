# Generated by Django 5.0.2 on 2024-05-02 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_suite_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suite',
            name='name',
            field=models.CharField(default='Suite', max_length=100),
        ),
    ]
