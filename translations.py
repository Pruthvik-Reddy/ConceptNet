import requests
from utils import *

concept="french_toast"
all_edges=get_all_edges_of_a_concept("french_toast")

translations=[]
for i in range(len(all_edges)):
  start=all_edges[i]["start"]["@id"]
  end=all_edges[i]["end"]["@id"]
  if start==concept:
    other=end
   
  else:
    other= start
  rel=all_edges[i]["rel"]["@id"]
  other_lang=other.split("/")[2]
  if other_lang !="en" and rel=="/r/Synonym":
    translations.append(other)
    print(other)
    