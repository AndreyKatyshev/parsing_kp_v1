from django.contrib import admin

from .models import Doc


class DocAdmin(admin.ModelAdmin):

    list_display = ('pk', 'authorId', 'movieId', 'id')
    search_fields = ('pk', 'authorId', 'movieId', 'id')
    empty_value_display = '-пусто-'


admin.site.register(Doc, DocAdmin)
