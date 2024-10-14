import networkx as nx
import matplotlib.pyplot as plt

# Створення неорієнтованого графа
G = nx.Graph()

# Додавання вершин (наприклад, зупинки або станції)
G.add_nodes_from(["Station A", "Station B", "Station C", "Station D", "Station E"])

# Додавання ребер (наприклад, маршрути між зупинками)
G.add_edges_from([
    ("Station A", "Station B"),
    ("Station A", "Station C"),
    ("Station B", "Station D"),
    ("Station C", "Station D"),
    ("Station C", "Station E"),
    ("Station D", "Station E")
])

# Завдання 1

# Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=15)
plt.title("Transport Network Graph")
plt.show()


# Завдання 2

def dfs(graph, start, target, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == target:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, target, path, visited)
            if result:
                return result

    path.pop()
    return None

def bfs(graph, start, target):
    queue = [(start, [start])]
    visited = set()

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor == target:
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))

    return None

# Використання алгоритмів
dfs_path = dfs(G, "Station A", "Station E")
bfs_path = bfs(G, "Station A", "Station E")

print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)


# Завдання 3

# Додавання ваг для ребер
G.add_weighted_edges_from([
    ("Station A", "Station B", 4),
    ("Station A", "Station C", 2),
    ("Station B", "Station D", 5),
    ("Station C", "Station D", 8),
    ("Station C", "Station E", 10),
    ("Station D", "Station E", 2)
])

# Знаходження найкоротшого шляху з використанням алгоритму Дейкстри
shortest_path = nx.dijkstra_path(G, source="Station A", target="Station E")
path_length = nx.dijkstra_path_length(G, source="Station A", target="Station E")

print("Найкоротший шлях за Дейкстром:", shortest_path)
print("Довжина найкоротшого шляху:", path_length)
