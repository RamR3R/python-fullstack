list  = [0,0,0,1,1,2,2,3]

# print(len(set(list))) # O(n) sc=> O(n)

fixed_pointer = 1
for i in range(1,len(list)):
    if list[i-1] != list[i]:
        list[fixed_pointer] = list[i]
        fixed_pointer += 1
print(fixed_pointer) #TC = O(n) SC = O(1)