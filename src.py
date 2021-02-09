import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from networkx.algorithms import community
import pickle


G = nx.Graph()
i = 0
with open('web-Stanford.csv', 'r') as f:
    
    lines = f.readlines()
    for edge in lines[4:]:
        i+= 1
        #print(edge.split())
        G.add_edges_from([edge.split()])
        #if i == 10000:
        #    break
print(G.number_of_nodes())
print(G.number_of_edges())



def save_file(to_save, name):
    
    with open(name, 'wb') as handle:
        pickle.dump(to_save, handle, protocol=pickle.HIGHEST_PROTOCOL)

		

		
pr = nx.pagerank(G, alpha=0.9)
max_key = max(pr, key=pr.get)
print(max_key)

save_file(pr, "pageRank.pickle")




comp = community.girvan_newman(G)
first_pair = tuple(sorted(c) for c in next(comp))

save_file(first_pair, 'girvan_newman.pickle')






#G = nx.karate_club_graph()
#coms = algorithms.infomap(G)





