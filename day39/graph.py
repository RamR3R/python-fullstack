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