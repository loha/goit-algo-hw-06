import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
G = nx.Graph()

# Додавання вершин (наприклад, 10 вершин)
nodes = range(1, 11)
G.add_nodes_from(nodes)

# Додавання ребер (зв'язки між вершинами)
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (7, 10), (8, 10), (9, 10)]
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray')
plt.title('Інтернет-топологія')
plt.show()

# Аналіз основних характеристик графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"Вершина {node}: ступінь {degree}")

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Вибір початкової та кінцевої вершин для пошуку шляхів
start_node = 1
goal_node = 10

# Пошук шляхів за допомогою DFS
dfs_result = list(dfs_paths(G, start_node, goal_node))

# Пошук шляхів за допомогою BFS
bfs_result = list(bfs_paths(G, start_node, goal_node))

print("DFS Paths:")
for path in dfs_result:
    print(path)

print("\nBFS Paths:")
for path in bfs_result:
    print(path)

# Аналіз результатів
print(f"Кількість шляхів, знайдених DFS: {len(dfs_result)}")
print(f"Кількість шляхів, знайдених BFS: {len(bfs_result)}")

# Порівняння першого знайденого шляху
print("\nПерший шлях, знайдений DFS:")
print(dfs_result[0] if dfs_result else "Шлях не знайдено")

print("\nПерший шлях, знайдений BFS:")
print(bfs_result[0] if bfs_result else "Шлях не знайдено")

