import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json


def scrape_top_list():
    responce=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
    soup=BeautifulSoup(responce.content,"html.parser")
    main=soup.find("tbody",class_="lister-list")
    movi=main.findAll("tr")
    moviList=[]
    for mov in movi:
        data={}
        movie=mov.find("a")
        movieName=movie.find("img")["alt"]
        movie_year=mov.find('span',class_="secondaryInfo").get_text().strip("()")
        movie_link=movie["href"]
        movie_rating=mov.find("strong").text
        movie_rank=mov.find("span")["data-value"]
        data["name"]=movieName
        data["rank"]=movie_rank
        data["year"]=movie_year
        data['rating']=movie_rating
        data["link"]=movie_link
        moviList.append(data)
    return moviList
        # with open ('all_movie.json','w') as f:
        #     json.dump(moviList,f,indent=4)

# scrape_top_list()


