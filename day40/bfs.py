#BFS 
from collections import deque
n = 8
edges = [(1,2) , (1,4) , (1,5) , (2,3) ,(3,7)
         , (4,6) , (5,6), (6,8),(8,7)
         ]

adj = {}
for i in range(1,n+1):
    adj[i] = []

for i in edges:
    u , v = i
    adj[u].append(v)
    #undirected graph
    adj[v].append(u)

print("\n",adj)


def bfs(node , adj , n):
    queue = deque([node])
    visited = {} 
    for i in range(1,n+1):
        visited[i] = False
    visited[node] = True # the starting point
    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        v = adj[current]
        for i in v: #adj list getting iterated
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
    print(result)
         


#BFS using Visisted as Array:

def BFS(node , adj , n):
    queue = deque([node])
    visited = [0] * n
    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        for i in adj[current]: #adj list getting iterated
            if not visited[i]: queue.append(i)
    
    return result

bfs(2 , adj , n)
