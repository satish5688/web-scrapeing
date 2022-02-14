import json
from pprint import pprint
with open("task9_all.json", "r") as f:
    movies = json.load(f)

genre={}
for s in movies:
    for v in s['movie genere']:
        if v in genre:
            genre[v]+=1
        else:
            genre[v]=1   
pprint(genre)
