import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes with labels
G.add_node(0, label='A', color='red')
G.add_node(1, label='A')
G.add_node(2, label='A')

# Add edges
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 0)

# Set the node labels
labels = nx.get_node_attributes(G, 'label')

# Draw the graph
pos = nx.spring_layout(G)  # positions for the nodes
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels)

# Show the graph
plt.axis('off')
plt.show()
