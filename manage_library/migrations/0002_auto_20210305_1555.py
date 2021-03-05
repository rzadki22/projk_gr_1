# Generated by Django 3.1.7 on 2021-03-05 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookcase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_library.bookcase'),
        ),
        migrations.AddField(
            model_name='book',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_library.room'),
        ),
        migrations.AddField(
            model_name='shelf',
            name='number',
            field=models.TextField(default='1', max_length=3),
            preserve_default=False,
        ),
    ]