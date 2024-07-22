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
