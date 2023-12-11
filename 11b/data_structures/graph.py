import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

L = ["A", "B", "C", "A"]

for i in range(0, len(L)):
    print(i)
    G.add_node(i, label=L[i])

G.add_node(3, label="A")
edge_list = [(0, 1), (1, 2), (2, 3), (3, 0)]
G.add_edges_from(edge_list)

labelsDict = dict(enumerate(L))
print(labelsDict)

nx.draw(
    G, 
    labels=labelsDict, 
    with_labels=True,
    node_color='lightgreen',
    #edge_color='b',
    #node_size = 1000,
    #width = 4
)
plt.show()