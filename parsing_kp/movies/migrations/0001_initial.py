# Generated by Django 4.1.3 on 2022-11-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('externalId', models.JSONField()),
                ('logo', models.JSONField()),
                ('poster', models.JSONField()),
                ('backdrop', models.JSONField()),
                ('rating', models.JSONField()),
                ('votes', models.JSONField()),
                ('videos', models.JSONField()),
                ('budget', models.JSONField()),
                ('fees', models.JSONField()),
                ('distributors', models.JSONField()),
                ('premiere', models.JSONField()),
                ('images', models.JSONField()),
                ('watchability', models.JSONField()),
                ('collections', models.JSONField()),
                ('updateDates', models.JSONField()),
                ('status', models.JSONField()),
                ('movieLength', models.JSONField()),
                ('productionCompanies', models.JSONField()),
                ('spokenLanguages', models.JSONField()),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(max_length=100, verbose_name='Тип или категоря')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('slogan', models.CharField(max_length=150, verbose_name='Слоган')),
                ('year', models.DateField(db_index=True, verbose_name='Год выхода')),
                ('facts', models.JSONField()),
                ('genres', models.JSONField()),
                ('countries', models.JSONField()),
                ('seasonsInfo', models.JSONField()),
                ('lists', models.JSONField()),
                ('typeNumber', models.FloatField()),
                ('alternativeName', models.CharField(max_length=150, verbose_name='Альтернативное название')),
                ('enName', models.JSONField()),
                ('names', models.JSONField()),
                ('sequelsAndPrequels', models.JSONField()),
                ('updatedAt', models.DateTimeField()),
                ('similarMovies', models.JSONField()),
                ('ratingMpaa', models.CharField(max_length=150, null=True)),
                ('shortDescription', models.CharField(max_length=150, null=True)),
                ('technology', models.JSONField()),
                ('ticketsOnSale', models.BooleanField()),
                ('imagesInfo', models.JSONField()),
                ('ageRating', models.CharField(max_length=150, null=True, verbose_name='Возрастной рейтинг')),
                ('top10', models.CharField(max_length=150, null=True, verbose_name='ТОП 10')),
                ('top250', models.CharField(max_length=150, null=True, verbose_name='ТОП 250')),
                ('createDate', models.DateTimeField(verbose_name='Дата создания')),
                ('releaseYears', models.DateField(db_index=True, verbose_name='Год релиза')),
                ('persons', models.ManyToManyField(related_name='movies', to='persons.person', verbose_name='Люди')),
            ],
        ),
    ]
