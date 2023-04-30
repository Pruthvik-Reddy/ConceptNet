import requests

def get_all_edges_of_a_concept(concept,language="en"):
    all_edges=[]
    uri='http://api.conceptnet.io/c/'+language+"/"+concept
    obj = requests.get(uri).json()
    

    edges=obj["edges"]
    for i in edges:
        all_edges.append(i)
        
        
        
    while "nextPage" in obj["view"]:
        nextpage=obj["view"]["nextPage"]
        next_uri="http://api.conceptnet.io"+nextpage
        obj=requests.get(next_uri).json()
        edges=obj["edges"]
        for i in edges:
            all_edges.append(i)
        if "nextPage" in obj["view"]:
            nextpage=obj["view"]["nextPage"]
        
    return all_edges


def get_all_edges_for_a_start_node_and_relation(start_node,relation,language="en"):
    offset = 0
    all_edges = []
    limit=100
    while True:
        url = f'http://api.conceptnet.io/query?start=/c/{language}/{start_node}&rel={relation}&limit={limit}&offset={offset}'
        response = requests.get(url).json()
        edges = response['edges']
        all_edges.extend(edges)
        
        if len(edges) < limit:
            break
        offset += limit
        #print(len(all_edges))
    return all_edges


def get_all_edges_for_a_end_node_and_relation(end_node,relation,language="en"):
    offset = 0
    all_edges = []
    limit=100
    while True:
        url = f'http://api.conceptnet.io/query?end=/c/{language}/{end_node}&rel={relation}&limit={limit}&offset={offset}'
        response = requests.get(url).json()
        edges = response['edges']
        all_edges.extend(edges)
        
        if len(edges) < limit:
            break
        offset += limit
        #print(len(all_edges))
    return all_edges



def get_all_edges_between_start_node_and_end_node(start_node,end_node,language="en"):
        
    all_edges=[]
    
    limit = 1000
    offset=0
    
    api_endpoint = 'http://api.conceptnet.io/query'
    while True:
        query_params = {
            'start': "/c/"+language+"/"+start_node,
            'end': "/c/"+language+"/"+end_node,
            'limit': limit,
            "offset":offset
        }

        response = requests.get(api_endpoint, params=query_params)

        edges = response.json()['edges']
        if len(edges)!=0:
            all_edges.extend(edges)
        offset+=limit
        if len(edges)==0 or len(edges)<limit:
            break

    return all_edges
    
def get_all_edges_for_startnode_endnode_and_relation(start_node,end_node,relation,language="en"):
    all_edges=[]
    
    limit = 1000
    offset=0
    
    api_endpoint = 'http://api.conceptnet.io/query'
    while True:
        query_params = {
            'start': "/c/"+language+"/"+start_node,
            'end': "/c/"+language+"/"+end_node,
            'limit': limit,
            "offset":offset,
            "rel": relation
        }

        response = requests.get(api_endpoint, params=query_params)

        edges = response.json()['edges']
        if len(edges)!=0:
            all_edges.extend(edges)
        offset+=limit
        if len(edges)==0 or len(edges)<limit:
            break

    return all_edges
    

def get_all_relations_between_start_and_end_node(start_node,end_node):
    all_relations=[]
    all_edges=get_all_edges_between_start_node_and_end_node(start_node,end_node)
    for i in range(len(all_edges)):
        relation=all_edges[i]["rel"]["@id"]
        all_relations.append(relation)
    return all_relations



def get_all_end_nodes_for_start_node_and_relation(start_node,relation):
    all_edges=get_all_edges_for_a_start_node_and_relation(start_node,relation)
    end_nodes=[]
    for i in range(len(all_edges)):
        end_nodes.append(all_edges[i]["end"]["@id"])
    return end_nodes

def get_all_start_nodes_for_end_node_and_relation(end_node,relation):
    all_edges=get_all_edges_for_a_end_node_and_relation(end_node,relation)
    start_nodes=[]
    for i in range(len(all_edges)):
        start_nodes.append(all_edges[i]["start"]["@id"])
    return start_nodes





