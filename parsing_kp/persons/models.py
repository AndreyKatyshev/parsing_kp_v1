from django.db import models


class Person(models.Model):
    spouses = models.JSONField()
    id = models.IntegerField(primary_key=True,)
    v = models.IntegerField()
    age = models.IntegerField(verbose_name='Возраст')
    birthPlace = models.JSONField(verbose_name='Место Рождения')
    birthday = models.DateTimeField(verbose_name='День Рождения')
    countAwards = models.JSONField()
    createdAt = models.DateTimeField()
    death = models.CharField(
        max_length=50, null=True)
    deathPlace = models.JSONField()
    enName = models.CharField(
        max_length=100, verbose_name='Имя по Английски')
    facts = models.JSONField()
    growth = models.IntegerField(verbose_name='Рост')
    name = models.CharField(
        max_length=100, verbose_name='Имя')
    photo = models.URLField()
    profession = models.JSONField()
    sex = models.CharField(
        max_length=50, verbose_name='Пол')
    updatedAt = models.DateTimeField()


class PersonMiniModel(models.Model):
    id = models.IntegerField(primary_key=True)
    photo = models.URLField()
    name = models.CharField(
        max_length=100, verbose_name='Имя', null=True)
    enName = models.CharField(
        max_length=100, verbose_name='Имя по Английски')
    enProfession = models.CharField(
        max_length=100, verbose_name='Профессия по Английски')