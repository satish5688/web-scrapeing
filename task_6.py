import json
from pprint import pprint


# def  analyse_movies_language():
#     movie_list=get_movie_list_details()
#     language={}
#     a=1
#     for s in movie_list:
#         for v in s['languages']:
#             if v in language:
#                 language[v]+=1
#             else:
#                 language[v]=1   
#     return(language)
# pprint(analyse_movies_language())



with open ("task_5.json",'r') as f:
    object=json.load(f)
def  analyse_movies_language():

    language={}
    for s in object:
        for v in s['languages']:
            if v in language:
                language[v]+=1
            else:
                language[v]=1   
    return(language)
pprint(analyse_movies_language())




        


