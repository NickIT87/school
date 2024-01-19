import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вузлів та ребер
G.add_nodes_from([(1, {'pos': (0, 0)}),
                  (2, {'pos': (1, 2)}),
                  (3, {'pos': (3, 1)}),
                  (4, {'pos': (5, 2)}),
                  (5, {'pos': (6, 0)})])

G.add_edges_from([(1, 2, {'weight': 3}),
                  (1, 3, {'weight': 7}),
                  (2, 3, {'weight': 2}),
                  (2, 4, {'weight': 5}),
                  (3, 4, {'weight': 1}),
                  (3, 5, {'weight': 4}),
                  (4, 5, {'weight': 6})])

# Відображення графа
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_color='black')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Знайти оптимальний маршрут
optimal_route = nx.shortest_path(G, source=1, target=5, weight='weight')
optimal_distance = nx.shortest_path_length(G, source=1, target=5, weight='weight')

print(f"Оптимальний маршрут: {optimal_route}")
print(f"Оптимальна відстань: {optimal_distance}")

plt.show()