from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Жанры"""
    name = models.CharField('Жанр', max_length=150, unique=True)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Character(models.Model):
    """Персонажи"""
    name = models.CharField('Персонаж', max_length=150)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение персонажа', upload_to='characters/')
    url = models.SlugField(max_length=130, unique=True)

    def get_absolute_url(self):
        return reverse('character_info', kwargs={'slug': self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Author(models.Model):
    """Авторы"""
    name = models.CharField('Автор', max_length=150)
    birth_year = models.PositiveSmallIntegerField('Год рождения', default=1900)
    death_year = models.PositiveSmallIntegerField('Год смерти', blank=True, null=True)
    image = models.ImageField('Изображение автора', upload_to='characters/')
    url = models.SlugField(max_length=130, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    """Книги"""
    title = models.CharField('Книга', max_length=150)
    description = models.TextField('Описание')
    year = models.PositiveSmallIntegerField('Год публикации', blank=True, null=True)
    text = models.FileField('Текст', upload_to='files/', blank=True, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    image = models.ImageField("Изображение", upload_to="books/")
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    characters = models.ManyToManyField(Character, verbose_name='Персонажи', blank=True, null=True)
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.SET_NULL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('book_info', kwargs={'slug': self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.book}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"