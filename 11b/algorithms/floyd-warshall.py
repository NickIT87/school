# import networkx as nx
# import matplotlib.pyplot as plt

# # Create a directed graph
# G = nx.DiGraph()

# # Add edges with weights
# G.add_edge(0, 1, weight=2)
# G.add_edge(0, 3, weight=1)
# G.add_edge(1, 2, weight=3)
# G.add_edge(2, 4, weight=4)
# G.add_edge(3, 2, weight=5)

# # Use Floyd-Warshall algorithm to find all-pairs shortest paths
# shortest_paths = nx.floyd_warshall(G, weight='weight')

# # Plot the graph
# pos = nx.spring_layout(G)  # Set the layout for the graph
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black')

# # Add edge labels with weights
# edge_labels = {(i, j): f"{d['weight']}" for i, j, d in G.edges(data=True)}
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Output the results and show the plot
# for source, targets in shortest_paths.items():
#     for target, shortest_path_length in targets.items():
#         if source != target:
#             print(f"Shortest path from {source} to {target}: {shortest_path_length}")

# plt.show()


# INF = float('inf')

# def floyd_warshall(graph):
#     num_vertices = len(graph)
    
#     # Инициализация матрицы расстояний
#     distance_matrix = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(num_vertices)] for i in range(num_vertices)]
    
#     # Проход по всем вершинам для поиска кратчайших путей
#     for k in range(num_vertices):
#         for i in range(num_vertices):
#             for j in range(num_vertices):
#                 # Если путь через вершину k короче, обновляем расстояние
#                 if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
#                     distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
    
#     return distance_matrix

# # Пример использования
# graph = [
#     [0, 2, 0, 1, 0],
#     [0, 0, 3, 0, 0],
#     [0, 0, 0, 0, 4],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

# result = floyd_warshall(graph)

# # Вывод результатов
# for row in result:
#     print(row)


import numpy as np
import matplotlib.pyplot as plt

def floyd_warshall(graph):
    n = len(graph)
    dist = np.copy(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]

    return dist

def visualize(graph, shortest_paths):
    fig, ax = plt.subplots()

    ax.set_xticks(np.arange(len(graph)))
    ax.set_yticks(np.arange(len(graph)))

    ax.set_xticklabels([str(i) for i in range(len(graph))])
    ax.set_yticklabels([str(i) for i in range(len(graph))])

    cax = ax.matshow(shortest_paths, cmap='viridis')

    for i in range(len(graph)):
        for j in range(len(graph)):
            plt.text(j, i, str(graph[i, j]) if graph[i, j] != float('inf') else '∞',
                     ha='center', va='center', color='black' if i != j else 'white')

    plt.title('Floyd-Warshall Shortest Paths')
    plt.colorbar(cax)

    plt.show()

if __name__ == "__main__":
    # Приклад графу, де float('inf') представляє нескінченність
    graph = np.array([
        [0, 3, float('inf'), 7],
        [8, 0, 2, float('inf')],
        [5, float('inf'), 0, 1],
        [2, float('inf'), float('inf'), 0]
    ])

    shortest_paths = floyd_warshall(graph)
    print("Матриця найкоротших шляхів:")
    print(shortest_paths)

    visualize(graph, shortest_paths)


