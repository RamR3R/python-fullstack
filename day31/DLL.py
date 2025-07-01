class Node:
    def __init__(self, val = 0, next = None , prev = None):
        self.val = val
        self.next = next
        self.prev = prev

item1 = Node(1)
item2 = Node(2)
item3 = Node(3)

item1.next = item2
item2.next = item3
item2.prev = item1
item3.prev = item2 

head = item1
current = head
result = []
tail = 0
while current != None:
    result.append(str(current.val))
    if current.next == None:
        tail = current

    current = current.next

print(' => '.join(result))

result = []
current = tail
while current != None:
    result.append(str(current.val))
    current = current.prev

print(' => '.join(result))