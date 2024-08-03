import heapq

def dijkstra(graph, start):
    # Ініціалізація
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    prev = [-1] * n
    pq = [(0, start)]  # (distance, vertex)
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        # Якщо знайдене значення більше, ніж вже відомий шлях, пропустити
        if current_dist > dist[u]:
            continue
        
        # Перевірити сусідів
        for v, weight in graph[u]:
            distance = current_dist + weight
            
            # Якщо знайдений коротший шлях
            if distance < dist[v]:
                dist[v] = distance
                prev[v] = u
                heapq.heappush(pq, (distance, v))
    
    return dist, prev

# Граф у вигляді списку суміжності
# graph[u] містить пари (v, weight), де weight - вага ребра між u і v
graph = {
    0: [(1, 4), (2, 1)],
    1: [(2, 2), (3, 5)],
    2: [(1, 2), (3, 8), (4, 10)],
    3: [(4, 2)],
    4: []
}

start_vertex = 0
distances, predecessors = dijkstra(graph, start_vertex)

print("Відстані від початкової вершини:")
for i, dist in enumerate(distances):
    print(f"До вершини {i}: {dist}")

print("\nПопередники у найкоротшому шляху:")
for i, prev in enumerate(predecessors):
    print(f"Вершина {i} попередник: {prev}")
