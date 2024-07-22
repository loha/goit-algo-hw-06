import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
G = nx.Graph()

# Додавання вершин (наприклад, 10 вершин)
nodes = range(1, 11)
G.add_nodes_from(nodes)

# Додавання ребер з вагами (зв'язки між вершинами з вагами)
edges = [(1, 2, 7), (1, 3, 9), (2, 4, 10), (2, 5, 15), (3, 6, 11), (4, 7, 6),
         (5, 8, 9), (6, 9, 14), (7, 10, 2), (8, 10, 3), (9, 10, 4)]
G.add_weighted_edges_from(edges)

# Візуалізація графу
pos = nx.spring_layout(G)  # Лейаут для розміщення графу
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Інтернет-топологія з вагами')
plt.show()

def dijkstra_shortest_paths(graph, start):
    # Використовуємо вбудовану функцію алгоритму Дейкстри з бібліотеки NetworkX
    length, path = nx.single_source_dijkstra(graph, start)
    return length, path

# Вибір початкової вершини для знаходження найкоротших шляхів до всіх інших вершин
start_node = 1

# Виконання алгоритму Дейкстри
lengths, paths = dijkstra_shortest_paths(G, start_node)

# Виведення результатів
print(f"Найкоротші шляхи від вершини {start_node} до всіх інших вершин:")
for target_node in paths:
    print(f"До вершини {target_node}: шлях {paths[target_node]}, довжина {lengths[target_node]}")

# Створення графу
G = nx.Graph()

# Додавання вершин (наприклад, 10 вершин)
nodes = range(1, 11)
G.add_nodes_from(nodes)

# Додавання ребер з вагами (зв'язки між вершинами з вагами)
edges = [(1, 2, 7), (1, 3, 9), (2, 4, 10), (2, 5, 15), (3, 6, 11), (4, 7, 6),
         (5, 8, 9), (6, 9, 14), (7, 10, 2), (8, 10, 3), (9, 10, 4)]
G.add_weighted_edges_from(edges)

# Візуалізація графу
pos = nx.spring_layout(G)  # Лейаут для розміщення графу
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Інтернет-топологія з вагами')
plt.show()

# Реалізація алгоритму Дейкстри
def dijkstra_shortest_paths(graph, start):
    # Використовуємо вбудовану функцію алгоритму Дейкстри з бібліотеки NetworkX
    length, path = nx.single_source_dijkstra(graph, start)
    return length, path

# Вибір початкової вершини для знаходження найкоротших шляхів до всіх інших вершин
start_node = 1

# Виконання алгоритму Дейкстри
lengths, paths = dijkstra_shortest_paths(G, start_node)

# Виведення результатів
print(f"Найкоротші шляхи від вершини {start_node} до всіх інших вершин:")
for target_node in paths:
    print(f"До вершини {target_node}: шлях {paths[target_node]}, довжина {lengths[target_node]}")

