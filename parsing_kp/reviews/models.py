from django.db import models

from movies.models import Movie


class Doc(models.Model):
    userRating = models.FloatField()
    a_id = models.CharField(
        max_length=100, verbose_name='ID неустановленного назначения _id')
    id = models.FloatField(primary_key=True)
    movieId = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='id_rn', 
        verbose_name='id фильма',
    )
    title = models.CharField('заголовок отзыва', max_length = 250)
    type = models.CharField('характер отзыва', max_length = 250)
    review = models.TextField('Текст записи',)
    date = models.DateTimeField('Дата создания')
    author = models.CharField('никнейм автора', max_length = 250)
    a_v = models.FloatField('поле неустановленного назначения __v')
    reviewDislikes = models.IntegerField()
    reviewLikes = models.IntegerField()
    updatedAt = models.DateTimeField('updatedAt')
    authorId = models.IntegerField()


class Review(models.Model):
    docs = models.ForeignKey(
        Doc,
        on_delete=models.CASCADE,
        related_name='id_rn',
        verbose_name='отзывы',
    )
    total = models.IntegerField()
    limit = models.IntegerField()
    page = models.IntegerField()
    pages = models.IntegerField()
