arr1 = [1,2,3,4,6,7]
arr2 = [5,6,7,8,9,10]

arr1.extend(arr2) #O(n)
arr1.sort() #O(nlog(n))
print(arr1)
result = [ ]
# TC = O(nlog(n))  => O(n)  SC = X