# Head Node[1,next] => [2,next] => [3,next] => tail Node [4, None]

class Node:
    def __init__(self , value = 0 , nextNode = None):
        self.val = value
        self.next = nextNode    

# item1 = Node(100) #head
# item2 = Node(200)
# item3 = Node(300)
# item4 = Node(400)
# item5 = Node(500) #tail node

# item1.next = item2
# item2.next = item3
# item3.next = item4
# item4.next = item5

head = Node(100) # head node
head.next = Node(200)
head.next.next = Node(300)
head.next.next.next = Node(400)
head.next.next.next.next = Node(500) #tail node

result = []

current = head

while current != None:
    print(current.val , end=" ") #current value will be printed
    current = current.next

# print('=>'.join(result))

# print(head)