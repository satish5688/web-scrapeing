import json,random,time, os
from ssl import DER_cert_to_PEM_cert
from task_4 import scrape_movie_details
with open ('all_movie.json') as file:
    movie=json.load(file)

def movie_folder():
    ml = []
    for x in movie:
        b=x['link'][7:-1]
        c="Movies/"+ b+".json"
        print(c)
        if os.path.exists(c):
            data = json.loads(open(c).read())
        else:
            data=scrape_movie_details(f'https://www.imdb.com/{x["link"]}')
            s=open(c,'w')
            s.write(json.dumps(data,indent=4))
            tim=random.randint(1,3)
            time.sleep(tim)
        ml.append(data)
    # with open("task9_all.json", "w") as f:
    #     json.dump(ml, f, indent=4)
    return ml
    
