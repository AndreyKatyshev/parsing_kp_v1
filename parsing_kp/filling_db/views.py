import os
import requests

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dotenv import load_dotenv



def seve_movie(request, movie_id):
    load_dotenv()
    open_token = 'ZQQ8GMN-TN54SGK-NB3MKEC-ZKB8V06'
    my_token = os.getenv('MY_TOKEN')
    id = movie_id
    base_url = 'https://api.kinopoisk.dev/movie'
    url_movie_kp = f'{base_url}?token={open_token}&search={id}&field=id'
    response = requests.get(url_movie_kp).json()
    return JsonResponse(response)