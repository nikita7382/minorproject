import requests
# from .models import Movie

# fetch poster from API
# api key:b6494834a468254130057f91b8b17c05


def fetch_poster(movie_id):
    r=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=b6494834a468254130057f91b8b17c05&language=en-US').json()
    return "https://image.tmdb.org/t/p/w500/"+r['poster_path']


# movie=Movie.objects.filter(movie_id=285)
print(fetch_poster(11450))
