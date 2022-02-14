
from task_1 import scrape_top_list
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json

def get_movie_list_details():
    scrap_top= scrape_top_list()
    movies_detail=[]
    for s in scrap_top[:50]:
        movie_info={}
        resp=requests.get(f"https://www.imdb.com/{s['link']}")
        soup=BeautifulSoup(resp.content,"html.parser")
        main=soup.find('div', class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
        Name=soup.find("h1").get_text()
        movie_info['moviename ']=Name
        b = main.find('ul', class_="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt")
        for s in b:
            c=s.get_text()
        Runtime=c
        movie_info['movie time']=Runtime
        poster=soup.find("img",class_="ipc-image")["src"]
        Poster_URL='www.imdb.com'+poster
        movie_info['Poster URL']=Poster_URL
        genere=soup.find("li",attrs={"data-testid":"storyline-genres"})
        a=genere.findAll("a")
        l=[]
        for i in a:
            g=i.text
            l.append(g)    
        movie_info['movie genere']=l
        Bio=soup.find('span',class_="GenresAndPlot__TextContainerBreakpointXL-sc-cum89p-2 eqbKRZ").text
        movie_info['Bio']=Bio
        dr=soup.find('div',class_="PrincipalCredits__PrincipalCreditsPanelWideScreen-sc-hdn81t-0 hzbDAm")
        Director=dr.find("div",class_="ipc-metadata-list-item__content-container").get_text()
        dir=soup.find('li',class_="ipc-metadata-list__item")
        Director=dir.findAll('a')
        li=[]
        for x in Director:
            b=x.text
            li.append(b)
        movie_info['movie director']=li

        details = soup.findAll("section", class_="ipc-page-section ipc-page-section--base celwidget")
        for d in details:
            if "data-testid" in d.attrs:
                if d.attrs['data-testid'] == "Details":
                    details_ul = d.findAll("li", class_="ipc-metadata-list__item")
                    for li in details_ul:
                            if "data-testid" in li.attrs:
                                if li.attrs['data-testid'] == "title-details-languages":
                                    deal = li.findAll("li", class_="ipc-inline-list__item")
                                    Detail = []
                                    if len(deal) > 0:
                                        for info in deal:
                                            Detail.append(info.text)
                                    movie_info['languages'] =Detail
                            if li.attrs['data-testid'] == "title-details-origin":
                                deal = li.findAll( "li", class_="ipc-inline-list__item")
                                Detail= []
                                if len(deal) > 0:
                                    for info in deal:
                                            Detail.append(info.text)
                                    movie_info['countries'] =Detail
        movies_detail.append(movie_info)
    return(movies_detail)
    # with open("task_5.json",'w') as f:
    #     json.dump(movies_detail,f,indent=4) 
get_movie_list_details()
