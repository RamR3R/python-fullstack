arr = [1,2,220,54,55,56,90,102]
target = 92

#best soln

index_dict = {} #sc => O(n)

for i in range(len(arr)): # O(n)
    index_dict[arr[i]] = i

for i in range(len(arr)): # O(n) => O(n) + O(n) => O(n) = TC
    find = target - arr[i] # SC => O(n)
    if find in index_dict and index_dict[find] != i: # O(1)
        print([i , index_dict[find]])
        break


# left = 0
# right = len(arr) - 1

# while left < right: # TC => O(n) SC => O(1)
#     if arr[left] + arr[right] < target:
#         left += 1
#     elif arr[left] + arr[right] > target:
#         right -= 1
#     else:
#         print([left, right])
#         break


for i in range(10,0,-1):
    print(i ,end=" ")