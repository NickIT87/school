import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    unvisited_nodes = list(graph.nodes)

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

# Приклад використання з графом
G = nx.Graph()
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=5)
G.add_edge('C', 'D', weight=1)

START_NODE = 'A'
result = dijkstra(G, START_NODE)

print(f"Shortest distances from {START_NODE}:")
for node, distance in result.items():
    print(f"To {node}: {distance}")


def plot_graph(graph):
    pos = nx.spring_layout(graph)  # Choose a layout for the nodes
    labels = nx.get_edge_attributes(graph, 'weight')  # Extract edge weights

    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    plt.show()


plot_graph(G)
