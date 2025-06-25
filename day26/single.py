arr = [0,2]
n = len(arr)
missing_number = (n* (n+1) // 2) - sum(arr)
print(missing_number)
#sc => O(1)
#TC => O(n) => 

# n(n+1)/2 2 => 2 * 3/2 => 6/2 => 3 - 2 => 1

# sum - sum(question) => missing


list = range(0 , len(arr) + 1) # [0,1,2]
#brute force soln
# for i in list: # O(n)
#     if i not in arr:  # O(n)
#         print(i)
# O(n * n) => O(n^2)
missing_number = arr[0]

for i in range(1,len(arr)): # O(n)
    missing_number = missing_number ^ arr[i]

for i in list: #O(n)
    missing_number = missing_number ^ i

#O(n + n) => O(2n) => O(n) O(1) TC , SC => O(n) O(1)

print(missing_number)






