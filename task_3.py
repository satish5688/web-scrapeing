
from task_1 import scrape_top_list
from pprint import pprint

def group_by_decade():
    scrap_top=scrape_top_list()
    decadewise={}

    # b=[]
    # for s in scrap_top:
    #     c=int(s['year'])
    #     b.append(c)
    # print(b)

    years=[int(s["year"]) for s in scrap_top]
    Min=min(years)
    Min_y=Min-(Min%10)
    Max=max(years)
    Max=Max-(Max%10)+10
    decade=list(range(Min_y,Max,10))
    for s in decade:
        for v in  scrap_top:
            if int(v['year'])>s and int(v['year'])<s+10:
                if str(s) not in decadewise:
                    decadewise[str(s)]=[v]
                else:
                    decadewise[str(s)].append(v)
    return(decadewise)
# pprint(group_by_decade())

