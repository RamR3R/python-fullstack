# Head Node[1,next] => [2,next] => [3,next] => tail Node [4, None]

class Node:
    def __init__(self , value = 0 , nextNode = None):
        self.val = value
        self.next = nextNode    

item1 = Node(100)
item2 = Node(200)
item3 = Node(300)
item4 = Node(400)
item5 = Node(500)

print(item3.val)