# from task_4 import scrape_movie_details
from task_1 import scrape_top_list
import _json
from bs4 import BeautifulSoup
import requests
from pprint import pprint
from task_12 import scrape_movie_cast


def scrape_movie_details(j):
    movie_info={}
    resp=requests.get(j)
    soup=BeautifulSoup(resp.content,"html.parser")
    Name=soup.find('div', class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt").h1.text
    movie_info['moviename ']=Name

    # b = main.find('ul', class_="ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt")
    # for s in b:
    #     c=s.get_text()
    # Runtime=c
    rnt=soup.find('li',attrs={'data-testid':"title-techspec_runtime"})
    Runtime=rnt.find('div',class_="ipc-metadata-list-item__content-container").text
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
    movie_info['Cast']=scrape_movie_cast()
    return(movie_info)
   
# pprint(scrape_movie_details('https://www.imdb.com/title/tt8176054/'))

