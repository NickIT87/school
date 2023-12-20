from collections import deque

def bfs(graph, start_vertex):
    visited = []
    queue = deque([start_vertex])

    while queue:
        current_vertex = queue.popleft()

        if current_vertex not in visited:
            print(current_vertex)
            visited.append(current_vertex)
            queue.extend(neighbor for neighbor in graph[current_vertex] 
                         if neighbor not in visited)

# # Приклад графа у вигляді словника зі списками сусідів
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Call BFS starting from vertex 'A'
bfs(graph, 'A')

# # Виклик рекурсивної функції для початку пошуку з вершини 'A'
# visited_vertices = []
# dfs(graph, 'A', visited_vertices)


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
# edges = list(nx.bfs_edges(G, source=1))
# # Використання DFS для отримання послідовності вершин
# bfs_nodes = list(nx.bfs_successors(G, source=1))

# # Виведення результатів
# print("BFS Nodes:", bfs_nodes)
# # Виведення результатів
# print("BFS Edges:", edges)

