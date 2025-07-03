arr = [4 ,12, 5, 3, 1, 2, 5 ,3, 1, 2 ,4 ,6]

maxStack = []

result = [-1] * len(arr)
print(result)

for i in range(len(arr)-1 , -1 , -1):

    while len(maxStack) !=0 and maxStack[-1] <= arr[i]:
        maxStack.pop()

    if len(maxStack) == 0:
        result[i] = -1
    else:
        result[i] = maxStack[-1]

    maxStack.append(arr[i])

print(arr)
print(result)
    