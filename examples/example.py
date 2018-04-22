import networkx as nx
from nbne import train_model

num_permutations = 10
graph = nx.watts_strogatz_graph(1000, 50, 0.2)
train_model(graph, num_permutations, 'watts_strogatz.emb')
