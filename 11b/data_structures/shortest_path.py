import networkx as nx
import matplotlib.pyplot as plt

G = nx.dodecahedral_graph()
# Assigning positive weights to edges
weights_pos = {(i, j): i + j for i, j in G.edges()}
# Assigning nonpositive weights to edges
weights_neg = {(i, j): -(i + j) for i, j in G.edges()}
# Specify edge colors based on weights
edge_colors = [weights_pos[edge] for edge in G.edges()]
# test cases 0 - 16 0 - 1
print(nx.shortest_path(G, source=0, target=16, method='dijkstra'))
print(nx.shortest_path(G, source=0, target=8, method='bellman-ford'))
# Draw the graph with edge colors based on weights
nx.draw(
    G,
    with_labels=True,
    font_color="white",
    edge_color=edge_colors,
    edge_cmap=plt.cm.Blues,  # You can choose a different colormap if needed
    width=2  # You can adjust the width of the edges
)
plt.show()
