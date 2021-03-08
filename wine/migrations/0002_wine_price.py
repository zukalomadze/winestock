# Generated by Django 3.1.7 on 2021-03-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='price',
            field=models.DecimalField(decimal_places=2, default=16, max_digits=6, verbose_name='price'),
            preserve_default=False,
        ),
    ]