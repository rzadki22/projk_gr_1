# Generated by Django 3.1.7 on 2021-03-07 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_library', '0009_auto_20210307_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookcase',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='room',
        ),
    ]