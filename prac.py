# a=['ComedyDrama']
# b=a[0].split('D')
# print(b)


# a=['sstd','tsgkg','jkfghjg','jkfhnf','jfjkkjf','raj','mir','ram','vansha','varsh','manisha','rekha','rasmika','rita']
# for s in a[5:10]:
#     print(s)



from task_5 import get_movie_list_details
import json

movie=get_movie_list_details()

data=json.dumps(movie, indent=4)
with open ("data.json",'w') as f:   
    f.write(data)




# from task_1 import scrape_top_list
# import json 

# movie=scrape_top_list()
# data=json.dumps(movie,indent=4)
# with open ("task_1.json",'w') as file:
#     file.write(f'{movie}')