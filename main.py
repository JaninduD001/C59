from collections import defaultdict

def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    visited = set()
    stack = []
    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]

def main():
    N = int(input().strip())
    constraints = [input().strip().split()[:3] for _ in range(N)]

    graph = defaultdict(list)
    for constraint in constraints:
        X, _, Y = constraint
        graph[X].append(Y)
        graph[Y].append(X)

    ordered_monsters = topological_sort(graph)
    print('\n'.join(ordered_monsters))

if __name__ == "__main__":
    main()
