import json
# from task_5 import get_movie_list_details
from task_4 import scrape_movie_details

with open ('all_movie.json') as file:
    movie=json.load(file)
# with open('task_5.json') as f:
    # object=json.load(f)
# data=scrape_movie_details()
# g=0
for x in movie:
    b=x['link'][7:-1]
    c="Movies/"+ b+".json"
    data=scrape_movie_details(f'https://www.imdb.com/{x["link"]}')
    s=open(c,'w')
    s.write(json.dumps(data,indent=4))
        


    

