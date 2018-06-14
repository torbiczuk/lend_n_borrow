from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from books.constants import RATING_VALUES


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=70)


class Library(models.Model):
    owner = models.ForeignKey(Person, verbose_name='Właściciel', on_delete=models.CASCADE, related_name='owner')
    book = models.ForeignKey(Book, verbose_name='Książka', on_delete=models.DO_NOTHING)
    borrowed = models.ForeignKey(Person, verbose_name='Pożyczono dla', on_delete=models.SET_DEFAULT,
                                 default='', related_name='borrowed')


class Rating(models.Model):
    owner = models.ForeignKey(Person, verbose_name='Autor oceny', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    rate = models.CharField(max_length=1, choices=RATING_VALUES, default='')

    class Meta:
        abstract = True


class BookRating(Rating):
    book = models.ForeignKey(Book, verbose_name='Książka', on_delete=models.CASCADE)

    def __str__(self):
        return 'Autor oceny: {} Książka: {} Ocena: {}'.format(self.owner, self.book, self.rate)


class UserRating(Rating):
    person = models.ForeignKey(Book, verbose_name='Użytkownik', on_delete=models.CASCADE)

    def __str__(self):
        return 'Autor oceny: {} Ocena: {} Oceniany: {}'.format(self.owner, self.rate, self.person)
