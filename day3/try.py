l = [1,2,3,2]
l.append(6)

print(l)

for i in l:
    print(i , end=" ")

l.remove(2)

print()

l.pop()

for i in range(0,len(l)):
    print(l[i] , end=" ")