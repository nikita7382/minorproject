import requests
# from .models import Movie

# fetch poster from API
# api key:b6494834a468254130057f91b8b17c05


def fetch_poster(movie_id):
    r=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=b6494834a468254130057f91b8b17c05&language=en-US').json()
    return ('https://image.tmdb.org/t/p/w500/'+r['poster_path'])

def fetch_overview(movie_id):
    r=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=b6494834a468254130057f91b8b17c05&language=en-US').json()
    return (r['overview'])
    
# movie=Movie.objects.filter(movie_id=285)
# print(fetch_overview(285))

# print('https://image.tmdb.org/t/p/w500/'+'/wdrCwmRnLFJhEoH8GSfymY85KHT.png')
