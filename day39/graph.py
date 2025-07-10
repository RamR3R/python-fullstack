# 1 => 2 , 2=>3 , 3 =>1 
n = 3
edges = [(1,2) , (2,3) , (3,1)]

adj = {}
for i in range(1,n+1):
    adj[i] = []

print(adj)

for i in edges:
    u , v = i
    print(u , v ,adj)
    adj[u].append(v)
    #undirected graph
    adj[v].append(u)

print("\n",adj)
n = 4
edges = [(1,2,2) , (2,3,3) , (3,4,4)]

adjMatrix = [ [0] * (n+1) for i in range(n+1)]

for i in edges:
    u , v , w = i
    adjMatrix[u][v] = w
    #undirected graph
    # adjMatrix[v][u] = w

for row in adjMatrix:
    print(row)

n = 4
edges = [(1,2,2) , (2,3,1) , (4,3,1) , (1,4,1)]

adj = {}
for i in range(1,n+1):
    adj[i] = []

for i in edges:
    u , v , w = i
    adj[u].append((v,w))

print(adj)

def isNeighbour(adj):
    start = int(input())
    end = int(input())
    #start = 2 end = 4 ans = -1

    for i in adj[start]:
        if i[0] == end:
            return i[1]

    return -1

print(isNeighbour(adj))
