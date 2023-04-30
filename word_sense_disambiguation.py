"""
NOTE : - Conceptnet does not include "sense_labels" for all nodes. It only has them for few. 
- In some cases, word senses are only distinguished by using parts of speech which is bare minimum. 

"""

import requests
concept="/c/en/cat"

uri="http://api.conceptnet.io/"+concept

obj=requests.get(uri).json()
all_edges=[]

while "nextPage" in obj["view"]:
  edges=obj["edges"]
  for i in edges:

    id1=i["end"]["@id"].split("/")[2]
    id2=i["start"]["@id"].split("/")[2]
    if id1=="en" and id2=="en":
      if i not in all_edges:
        all_edges.append(i)
  nextpage=obj["view"]["nextPage"]
  next_uri="http://api.conceptnet.io"+nextpage
  obj=requests.get(next_uri).json()


for i in range(len(all_edges)):
  if "sense_label" in all_edges[i]["end"]:
    if all_edges[i]["end"]["term"]=="/c/en/cat":
      print(all_edges[i]["start"]["term"])
      print(all_edges[i]["end"]["term"])
      print(all_edges[i]["end"]["sense_label"])
      print()
  if "sense_label" in all_edges[i]["start"]:
    if all_edges[i]["start"]["term"]=="/c/en/cat":
      print(all_edges[i]["start"]["term"])
      print(all_edges[i]["end"]["term"])
      print(all_edges[i]["start"]["sense_label"])
      print()