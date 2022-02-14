from task_1 import scrape_top_list
from pprint import pprint

def group_by_year():
    scrap_top=scrape_top_list()
    data={}
    for s in scrap_top:
        if s["Year"] not in data:
            data[s["Year"]]=[s]
        else:
            data[s["Year"]].append(s)
    return data