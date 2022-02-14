import json
from pprint import pprint

with open ("task_5.json",'r') as f:
    object=json.load(f)
def  analyse_movies_language():

    language={}
    for s in object:
        for v in s['movie director']:
            if v in language:
                language[v]+=1
            else:
                language[v]=1   
    return(language)
pprint(analyse_movies_language())
