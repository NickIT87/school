def dfs(graph, current_vertex, visited):
    if current_vertex not in visited:
        print(current_vertex)
        visited.append(current_vertex)
        for neighbor in graph[current_vertex]:
            dfs(graph, neighbor, visited)

# Приклад графа у вигляді словника зі списками сусідів
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Виклик рекурсивної функції для початку пошуку з вершини 'A'
visited_vertices = []
dfs(graph, 'A', visited_vertices)
print(visited_vertices)

# graph = [ [4, 5], [5], [3,4], [2,4], [0,2,3], [0,1] ]
# stan = [False for i in range(len(graph))]
# print(stan)
# print('Порядок обходу вершин')
# def func(v):
#     print(v)
#     stan[v] = True
#     for vertex in graph[v]:
#         if not stan[vertex]:
#             func(vertex)

# for c in range(len(graph)):
#     if not stan[c]:
#         func(c)

# print(stan)


# import networkx as nx

# # Створення графа
# G = nx.Graph()
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])

# # Використання DFS
# edges = list(nx.dfs_edges(G, source=1))
# # Використання DFS для отримання послідовності вершин
# dfs_nodes = list(nx.dfs_preorder_nodes(G, source=1))

# # Виведення результатів
# print("DFS Nodes:", dfs_nodes)
# # Виведення результатів
# print("DFS Edges:", edges)

