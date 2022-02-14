


import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup


# with open('all_movie.json','r') as f:
#     data=json.load(f)
# cast_link=[]
# for s in data:
#     info={}
#     req=requests.get(f"https://www.imdb.com/{s['link']}")
#     soup=BeautifulSoup(req.content,"html.parser")
#     cast=soup.find('li',class_="ipc-metadata-list__item ipc-metadata-list-item--link")
#     caste=cast.find('a')['href']
#     Name=soup.find('div', class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.text
#     info['Name']=Name
#     info['cast_link']=caste
#     cast_link.append(info)
# with open("cast-link.json", "w") as f:
#         json.dump(cast_link, f, indent=4)

def scrape_movie_cast(link):
    print(link)
    req=requests.get(link)
    soup=BeautifulSoup(req.content,"html.parser")
    data=soup.find('table',class_="cast_list")
    deta=data.findAll('tr')
    cast=[]
    for s in deta:
        info={}
        v=s.find("td",class_="")
        if v!=None:
            name=v.find("a").text[:-2]
            imdb_id=v.find("a")["href"][6:15]
            info['imdb_id']=imdb_id
            info['Name']=name
            cast.append(info)
    return(cast)
