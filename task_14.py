import json
from pprint import pprint
from task_12 import scrape_movie_cast

with open ('all_movie.json','r') as f:
    obj=json.load(f)
m_obj = {}
for s in  obj[:3]:
    cast_data = scrape_movie_cast(f'http://imdb.com{s["link"]}fullcredits/cast?ref_=tt_ov_st_sm')
    for ac in cast_data:
        if ac['imdb_id'] not in m_obj:
            m_obj[ac['imdb_id']] = {"name": ac['Name']}
            m_obj[ac['imdb_id']]['frequent_co_actors'] = []
            for fac in cast_data:
                if fac['imdb_id'] == ac['imdb_id']:
                    continue
                m_obj[ac['imdb_id']]['frequent_co_actors'].append({
                    "imdb_id": fac['imdb_id'],
                    "name": fac['Name'],
                    "num_movies": 1
                })
        else:
             for fac in cast_data:
                if fac['imdb_id'] == ac['imdb_id']:
                    continue
                for i in m_obj[ac['imdb_id']]['frequent_co_actors']:
                    if i['imdb_id'] == fac['imdb_id']:
                        i['num_movies']+=1
                        break
                else:
                     m_obj[ac['imdb_id']]['frequent_co_actors'].append({
                    "imdb_id": fac['imdb_id'],
                    "name": fac['Name'],
                    "num_movies": 1
                })
pprint(m_obj)