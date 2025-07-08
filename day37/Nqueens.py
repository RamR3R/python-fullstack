n = 4
board = [["."]*n for _ in range(n)]

def display():
    for i in board:
        print(i)
    print("\n")

def backtrack(row , colSet , posDiagonal , negDiagonal , board):
    #base condition
    if row == n:
        display()
        return
    
    for col in range(0,n):
        neg = row - col
        pos = row + col
        if col not in colSet and pos not in posDiagonal and neg not in negDiagonal :
            colSet.add(col)
            posDiagonal.add(pos)
            negDiagonal.add(neg)
            board[row][col] = "Q"
            backtrack(row + 1 ,colSet , posDiagonal , negDiagonal , board)
            colSet.remove(col)
            posDiagonal.remove(pos)
            negDiagonal.remove(neg)
            board[row][col] = "."
    
backtrack(0, set() , set() , set() , board)

