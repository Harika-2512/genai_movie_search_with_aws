import requests

def fetch_movie_data():
    #response = requests.get("http://vod-microservice/movies")
    #return response.json()

    response = [
    {
        "id": "mv001",
        "title": "Inception",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
        "genre": ["Action", "Sci-Fi", "Thriller"],
        "rating": 8.8,
        "description": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea."
    },
    {
        "id": "mv002",
        "title": "The Shawshank Redemption",
        "actors": ["Tim Robbins", "Morgan Freeman"],
        "genre": ["Drama"],
        "rating": 9.3,
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of decency."
    },
    {
        "id": "mv003",
        "title": "The Dark Knight",
        "actors": ["Christian Bale", "Heath Ledger"],
        "genre": ["Action", "Crime", "Drama"],
        "rating": 9.0,
        "description": "When the menace known as the Joker emerges from his mysterious past, he starts a reign of chaos on Gotham."
    },
    {
        "id": "mv004",
        "title": "The Hatred",
        "actors": ["Salman Khan"],
        "genre": ["Action", "Crime"],
        "rating": 7.0,
        "description": "Movie about hate."
    },
    {
        "id": "mv005",
        "title": "The Love",
        "actors": ["Shah Rukh khan", "Kajol"],
        "genre": ["Drama"],
        "rating": 6.0,
        "description": "Movie about love."
    }
    ]
    return response
