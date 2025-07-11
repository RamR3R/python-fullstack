edges = [(1,2) , (2,3) , (3,5) , (3,4),
         (4,6) , (6,7) , (7,8) , (7,9)]
n = 9
adj = {}
for i in range(1,n+1):
    adj[i] = []

for edge in edges:
    u , v = edge
    adj[u].append(v)
    adj[v].append(u)

print(adj)

def dfs(adj , node , visited = {}):
    print(node , end=" ") #result
    visited[node] = True

    for v in adj[node]:
        if v not in visited:
            dfs(adj , v , visited)

dfs(adj , 1 , {})