arr = [2,1,4,5,1,1,1,1,3,2]
target = 3
longest = 0

i = 0
j = 0
sub_sum = arr[i]
# while i < len(arr) - 1 and j < len(arr) - 1: #O(2N) => O(N)
    
#     if sub_sum < target:
#         j += 1
#         sub_sum += arr[j]
#     elif sub_sum > target:
#         sub_sum -= arr[i]
#         i += 1
#     else:
#         print(i,j)
#         longest = max(j - i + 1 , longest)
#         j += 1
#         sub_sum += arr[j]

sum = 0
prefix_sum = {}
arr = [-10,-1,-1,2,0,4,-1,8]
for x in range(0 , len(arr)):
    sum += arr[x]
    if sum == target:
        longest = x + 1
    else:
        if (sum - target) in prefix_sum:
            longest = max(longest , x - prefix_sum[sum-target])
    if sum not in prefix_sum:
        prefix_sum[sum] = x

print(arr)
print(longest)