import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

graph = np.array([
    [0, 3, float('inf'), 7],
    [8, 0, 2, float('inf')],
    [5, float('inf'), 0, 1],
    [2, float('inf'), float('inf'), 0]
])

G = nx.DiGraph()

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i, j] != float('inf'):
            G.add_edge(i, j, weight=graph[i, j])

pos = nx.spring_layout(G)
labels = {(i, j): f"{graph[i, j]:.0f}" if graph[i, j] != float('inf') else '∞' for i, j in G.edges}

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title('Graph Visualization')
plt.show()
