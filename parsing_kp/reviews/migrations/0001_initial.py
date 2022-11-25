# Generated by Django 4.1.3 on 2022-11-24 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('userRating', models.FloatField()),
                ('a_id', models.CharField(max_length=100, verbose_name='ID неустановленного назначения _id')),
                ('id', models.FloatField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, verbose_name='заголовок отзыва')),
                ('type', models.CharField(max_length=250, verbose_name='характер отзыва')),
                ('review', models.TextField(verbose_name='Текст записи')),
                ('date', models.DateTimeField(verbose_name='Дата создания')),
                ('author', models.CharField(max_length=250, verbose_name='никнейм автора')),
                ('a_v', models.FloatField(verbose_name='поле неустановленного назначения __v')),
                ('reviewDislikes', models.IntegerField()),
                ('reviewLikes', models.IntegerField()),
                ('updatedAt', models.DateTimeField(verbose_name='updatedAt')),
                ('authorId', models.IntegerField()),
                ('movieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_rn', to='movies.movie', verbose_name='id фильма')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('limit', models.IntegerField()),
                ('page', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('docs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_rn', to='reviews.doc', verbose_name='отзывы')),
            ],
        ),
    ]
