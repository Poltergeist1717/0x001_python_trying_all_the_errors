import requests_with_caching
import json

def get_movies_from_tastedive(content):
    base_url = "https://tastedive.com/api/similar"
    para = {"q" : content, "type" : "movies", "limit" : "5"}
    data = requests_with_caching.get(base_url, params = para)
    tastedive_movies = json.loads(data.text)
    return tastedive_movies

def extract_movie_titles(movies_dict):
    extracted_titles = list()
    try:
        titles = movies_dict['Similar']['Results']
        for title in titles:
            extracted_titles.append(title['Name'])
    except(TypeError, KeyError) as e:
        # Handle the error gracefully
        print(f"Error extracting movie titles: {e}")
    return extracted_titles

def get_related_titles(titles_list):
    if titles_list != []:
        related_list=[]
        extracted_related_list = []
        for title in titles_list:
            related_list = extract_movie_titles(get_movies_from_tastedive(title))
            for movieName in related_list:
                if movieName not in extracted_related_list:
                    extracted_related_list.append(movieName)

        return extracted_related_list
    return titles_list

def get_movie_data(movie_title):
    base_url = 'http://www.omdbapi.com/'
    para = {'t': movie_title, 'r' :'json'}
    data = requests_with_caching.get(base_url, params = para)
    movie_data = json.loads(data.text)
    return movie_data

def get_movie_rating(title_dict):
    rating = ""
    for rating_list in title_dict["Ratings"]:
        if rating_list["Source"]== "Rotten Tomatoes":
            rating = rating_list["Value"]
    if rating != "":
        int_rating = int(rating[:2])
    else: int_rating = 0
    return int_rating

def get_sorted_recommendations(titles):
    title_list = get_related_titles(titles)
    title_list = sorted(title_list, key = lambda title: (get_movie_rating(get_movie_data(title)), title), reverse=True)

    return title_list
