from django.contrib import admin

from .models import Movie


class MovieAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', 'id')
    search_fields = ('pk', 'name', 'id')
    empty_value_display = '-пусто-'


admin.site.register(Movie, MovieAdmin)
