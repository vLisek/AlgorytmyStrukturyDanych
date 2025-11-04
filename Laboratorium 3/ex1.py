graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}


def dfs(graph, start):
    visited = []

    def dfs_recursive(node):
        if node not in visited:
            visited.append(node)
            for neighbor in sorted(graph[node]):
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return visited


start_vertex = 'A'
dfs_order = dfs(graph, start_vertex)
print("Kolejność odwiedzania (DFS):", dfs_order)
