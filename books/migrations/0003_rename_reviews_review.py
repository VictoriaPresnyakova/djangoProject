# Generated by Django 4.2.7 on 2023-11-10 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
