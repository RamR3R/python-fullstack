mat = [[1,2,3,4] ,
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
mat2 = [[1,1,1] , [0,0,0], [0,0,1]]
n = 4
col = 4
result = []

# for i in range(0, row):
#     rowList = []
#     for j in range(0 , col):
#         rowList.append(mat1[i][j] + mat2[i][j])
#     result.append(rowList)
# for i in range(row):
#     for j in range(col):
#         if i == j or i + j == row - 1:
#             result += mat[i][j]

top = 0
bottom = n - 1
left = 0
right = n - 1

while top < bottom or left < right:
    for i in range(left , right + 1):
        result.append(mat[top][i])
    top += 1

    for i in range(top , bottom + 1):
        result.append(mat[i][right])
    right -= 1

    for i in range(right , left - 1 , -1):
        result.append(mat[bottom][i])
    bottom -= 1

    for i in range(bottom , top - 1 , -1):
        result.append(mat[i][left])
    left += 1


print(result)

