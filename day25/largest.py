list = [8,2,30,40,5,6,4]

max = list[0]
for i in range(1, len(list)):
    if max < list[i]:
        max = list[i]

print(max)
#  O(n)

list = [8,2,30,40,5,6,4,40,35]
# list.sort() # O(nlog(n))
max = list[0]
secondMax = list[0]
# O(n)
for i in range(len(list)): 
    if max < list[i]:
        secondMax = max
        max = list[i]
    elif list[i] > secondMax and list[i] != max:
        secondMax = list[i]

print(secondMax)


