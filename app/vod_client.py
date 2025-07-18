import requests

def fetch_movie_data():
    #response = requests.get("http://vod-microservice/movies")
    response = requests.get("http://vod_content:8000/movies")
    return response.json()

   