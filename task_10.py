from pprint import pprint
import json
with open("task9_all.json", "r") as f:
    movies = json.load(f)
directors = []
directors_and_movies = {}
for s in movies:
    for dirName in s["movie director"]:
        if dirName not in directors:
            directors.append(dirName)

for dir in directors:
    languages_count = {}

    for movie in movies:
        if dir in movie["movie director"]:
            for lang in movie["languages"]:
                if lang in languages_count:
                    languages_count[lang] += 1
                else:
                    languages_count[lang] = 1
    directors_and_movies[dir] = languages_count

pprint(directors_and_movies)