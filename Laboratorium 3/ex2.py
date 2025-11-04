from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}


def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in sorted(graph[node]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited


start_vertex = 'A'
bfs_order = bfs(graph, start_vertex)
print("Kolejność odwiedzania (BFS):", bfs_order)
