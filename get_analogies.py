import sys
import requests
from utils import *
from collections import Counter

word1=sys.argv[1]
word2=sys.argv[2]
word3=sys.argv[3]
symmetric_relations="Antonym,DistinctFrom,EtymologicallyRelatedTo,LocatedNear,RelatedTo, imilarTo,Synonym".split(",")
asymmetric_relations="AtLocation,CapableOf,Causes,CausesDesire,CreatedBy,DefinedAs,DerivedFrom,Desires,Entails,ExternalURL,FormOf,HasA,HasContext,HasFirstSubevent,HasLastSubevent,HasPrerequisite,HasProperty,InstanceOf,IsA,MadeOf,MannerOf,MotivatedByGoal,ObstructedBy,PartOf,ReceivesAction,SenseOf,SymbolOf,UsedFor".split(",")
for i in range(len(symmetric_relations)):
  symmetric_relations[i]="/r/"+symmetric_relations[i]
for i in range(len(asymmetric_relations)):
  asymmetric_relations[i]="/r/"+asymmetric_relations[i]


possible_relations_1=get_all_relations_between_start_and_end_node(word1,word2)

possible_relations_2=get_all_relations_between_start_and_end_node(word1,word3)

if len(possible_relations_1)==0 or len(possible_relations_2)==0:
    possible_relations_1=get_all_relations_between_start_and_end_node(word2,word1)
    possible_relations_2=get_all_relations_between_start_and_end_node(word3,word1)


possible_words_1=[]
possible_words_2=[]

print(possible_relations_1)
for i in possible_relations_1:
    if i in asymmetric_relations:
        rel=i
        end_nodes=get_all_end_nodes_for_start_node_and_relation(word2,rel)
        possible_words_1.extend(end_nodes)

    else: 
        rel=i
        nodes_1=get_all_end_nodes_for_start_node_and_relation(word2,rel)
        nodes_2=get_all_start_nodes_for_end_node_and_relation(word2,rel)
        possible_words_1.extend(nodes_1)
        possible_words_1.extend(nodes_2)
possible_words_1=list(set(possible_words_1))

for i in possible_relations_2:
    if i in asymmetric_relations:
        rel=i
        end_nodes=get_all_end_nodes_for_start_node_and_relation(word2,rel)
        possible_words_2.extend(end_nodes)

    else: 
        rel=i
        nodes_1=get_all_end_nodes_for_start_node_and_relation(word2,rel)
        nodes_2=get_all_start_nodes_for_end_node_and_relation(word2,rel)
        possible_words_2.extend(nodes_1)
        possible_words_2.extend(nodes_2)
possible_words_2=list(set(possible_words_2))

print(possible_words_1)
print(possible_words_2)

results=[]
for i in range(len(possible_words_1)):
  for j in range(len(possible_words_2)):
    if possible_words_2[j]==possible_words_1[i]:
      if possible_words_2[j].split("/")[3]!=word1 and possible_words_2[j].split("/")[2]=="en":
        results.append(possible_words_2[j])

print(results)

only_target_words=[]
for i in range(len(results)):
   word=results[i].split("/")[3]
   only_target_words.append(word)
string_counts=Counter(only_target_words)
most_common_string, count = max(string_counts.items(), key=lambda x: x[1])
print(most_common_string)
print(word1+ ":" + word2 + "::" + word3 + ":" + most_common_string)
