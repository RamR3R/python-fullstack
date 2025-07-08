maze = [
    [1,0,0,0],
    [1,1,1,1],
    [1,1,0,1],
    [0,1,1,1]
]
n = 4
visited = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(False)
    visited.append(row)

def rat_move(i , j , path):
    #Base Condition
    if maze[i][j] == 0:
        return
    if i == n-1 and j == n-1:
        print(path)
        return
    
    visited[i][j] = True
    #down movement
    if i != n-1 and visited[i+1][j] == False: rat_move(i+1 , j , path + "D")
    #right movement
    if j != n-1 and not visited[i][j+1]: rat_move(i , j + 1 , path + "R")
    #left movement
    if j != 0 and not visited[i][j-1]: rat_move( i , j -1 , path + "L")
    #up movement
    if i != 0 and not visited[i-1][j]: rat_move( i -1 , j , path + "U")
    visited[i][j] = False

rat_move(0,0,"")