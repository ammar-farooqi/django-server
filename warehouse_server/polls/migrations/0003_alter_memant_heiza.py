# Generated by Django 3.2.4 on 2021-06-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_memant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memant',
            name='heiza',
            field=models.IntegerField(default=0),
        ),
    ]
