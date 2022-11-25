from django.contrib import admin
from django.urls import path

from filling_db import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('save_movie/<int:movie_id>/', views.seve_movie, name = 'seve_movie')
]
