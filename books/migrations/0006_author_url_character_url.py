# Generated by Django 4.2.7 on 2024-02-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_characters'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='url',
            field=models.SlugField(default=123, max_length=130, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='url',
            field=models.SlugField(default=123, max_length=130),
            preserve_default=False,
        ),
    ]