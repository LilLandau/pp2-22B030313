def is_high_score(movie):
    if movie["imdb"] > 5.5:
        return True
    
    return False

def list_high_scores(movies):
    result = []

    for movie in movies:
        if movie["imdb"] > 5.5:
            result.append(movie["name"])
    
    return result

def show_films_by_category(movies, category):
    result = []

    for movie in movies:
        if movie["category"] == category:
            result.append(movie["name"])

    return result

def average_score_by_list(movies):
    amount_of_movies = len(movies)

    sum_of_score = 0

    for movie in movies:
        sum_of_score += movie["imdb"]

    return (sum_of_score/amount_of_movies)

def average_score_by_category(movies, category):
    movies_by_category = show_films_by_category(movies, category)
    
    return average_score_by_list(movies_by_category)


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]