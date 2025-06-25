list = [1,2,3,4,5,0,3,0,4,0,5,6]

# numbers = [] # n
# zeros = []   # n
# for i in range(len(list)):
#     if list[i] == 0:
#         zeros.append(0)
#     else:
#         numbers.append(list[i])
# numbers.extend(zeros)
# print(numbers)

# TC = O(n) Sc = (2n)

# result = []
# for i in range(len(list)):
#     if list[i] != 0:
#         result.append(list[i])
# #O(n)

# noOfZero = list.count(0)

# for i in range(noOfZero):
#     result.append(0)
#O(n) =>O(2n) => O(n)
#sc => O(n)

index = 0
for i in range(len(list)):
    if list[i] != 0:
        list[index] = list[i]
        index += 1

for i  in range(index , len(list)):
    list[i] = 0

print(list)

# TC => O(n) and SC => O(1)






# result => 1,2,3,4,5,3,4,5,6,0,0,0