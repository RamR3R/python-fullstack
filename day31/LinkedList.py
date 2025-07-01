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

# length = 0
def display_linked_list(current):
    result = []
    while current != None:
        result.append(str(current.val))
        current = current.next
    print(' => '.join(result))

#add item to the tail of LinkedList
# current = head
# while current.next != None:
#     current = current.next

# current.next = Node(int(input()))

# display_linked_list(head)

# newNode = Node(int(input()))
# newNode.next = head

# head = newNode

#insert at particular position
position = 1
value = 250

newNode = Node(value)
current = head
node_position = 0

# if position == 1:
#     newNode.next = head
#     head = newNode

# while current != None:
#     node_position += 1
#     if node_position == position - 1:
#         temp = current.next
#         current.next = newNode
#         newNode.next = temp
    
#     current = current.next

length = 0
current = head
while current != None:
    length += 1
    current = current.next

current = head
count = 0
while current != None:
    count += 1
    if count == length // 2 + 1:
        print("middle Element = " , current.val)
    current = current.next


display_linked_list(head)