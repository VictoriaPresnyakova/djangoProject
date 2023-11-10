# Generated by Django 4.2.7 on 2023-11-10 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_reviews_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='death_year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год смерти'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='text',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год публикации'),
        ),
    ]
