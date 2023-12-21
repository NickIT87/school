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

# пошук в ширину (підручник)
# Поиск в ширину

graph = [
    [1, 3],         # 0
    [0, 3, 4, 5],   # 1
    [4, 5],         # 2
    [0, 1, 5],      # 3
    [1, 2],         # 4
    [1, 2, 3]       # 5
]

start = [-1]*len(graph)
print('Початковий стан: ', start)

def func(s):
    global start
    start[s] = 0
    queue = [s]
    print('Динаміка зміну стану вершини')
    while queue:
        print(start)
        v = queue.pop(0)
        for m in graph[v]:
            if start[m] == -1:
                queue.append(m)
                start[m] = start[v] + 1


for i in range(len(graph)):
    if start[i] == -1:
        func(i)
    print('Вершина ', i, ', номер обходу ', start[i])




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

