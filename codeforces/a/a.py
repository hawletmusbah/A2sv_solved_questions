import sys
from collections import deque

def solve():
    # Increase recursion depth for deep trees if using DFS, 
    # but BFS is safer for large n.
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    if n == 1:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = int(input[idx])
        v = int(input[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    def bfs(start_node):
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = deque([start_node])
        
        farthest_node = start_node
        max_dist = 0
        
        while queue:
            curr = queue.popleft()
            if distances[curr] > max_dist:
                max_dist = distances[curr]
                farthest_node = curr
            
            for neighbor in adj[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)
                    
        return farthest_node, max_dist

    # First BFS to find one end of the diameter
    u, _ = bfs(1)
    # Second BFS to find the length of the diameter
    v, diameter = bfs(u)

    print(diameter * 3)

if __name__ == "__main__":
    solve()