import os
import requests

# from bs4 import BeautifulSoup
# преодразвоывает html сод в дерево объектов пайтон
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dotenv import load_dotenv

from movies.models import Movie
from persons.models import Person, PersonMiniModel

def seve_movie(request, movie_id):
    open_token = 'ZQQ8GMN-TN54SGK-NB3MKEC-ZKB8V06'
    id = movie_id
    base_url = 'https://api.kinopoisk.dev/movie'
    url_movie_kp = f'{base_url}?token={open_token}&search={id}&field=id'
    response = requests.get(url_movie_kp).json()
    persons = response.pop('persons')

    person_models = []
    for i in persons:  
        person_models.append(PersonMiniModel.objects.create(**i))
    movie = Movie.objects.create(**response)
    movie.persons.set(person_models)

    # return JsonResponse(response)



# def seve_movie_local(movie_id):
#     load_dotenv()
#     open_token = 'ZQQ8GMN-TN54SGK-NB3MKEC-ZKB8V06'
#     my_token = os.getenv('MY_TOKEN')
#     id = movie_id
#     base_url = 'https://api.kinopoisk.dev/movie'
#     url_movie_kp = f'{base_url}?token={open_token}&search={id}&field=id'
#     response = requests.get(url_movie_kp).json()

#     print(len(response))
#     print(type(response))
#     print(response['externalId'])
# seve_movie(505898)