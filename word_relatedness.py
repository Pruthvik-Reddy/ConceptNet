import requests

concepts=["dog","cat","cats","pet","river","bank","money"]

for i in range(len(concepts)-1):
  first=concepts[i]
  second=concepts[i+1]
  uri=f"https://api.conceptnet.io/relatedness?node1=/c/en/{first}&node2=/c/en/{second}"
  obj=requests.get(uri).json()
  print("Concept 1:",first,"Concept 2:",second,"Relatedness :",obj["value"])
