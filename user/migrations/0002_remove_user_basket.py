# Generated by Django 3.1.7 on 2021-03-05 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='basket',
        ),
    ]
