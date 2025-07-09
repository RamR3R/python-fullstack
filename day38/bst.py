class Node:
    def __init__(self , val = 0 , left = None , right = None):
        self.val = val
        self.left = left
        self.right = right

def preOrderTraversal(root):
    #base Condition
    if root == None:
        return
    
    print(root.val , end=" ") #root
    preOrderTraversal(root.left)  #left
    preOrderTraversal(root.right) #right


arr = [5,7,2,3,4,9,8]
root = Node(arr[0])

def insertNode(root , newVal):
    
    if root.left == None and newVal < root.val:
        root.left = Node(newVal)
        return
    
    if root.right == None and newVal > root.val:
        root.right = Node(newVal)
        return

    if newVal < root.val:
        insertNode(root.left , newVal)
    if newVal > root.val:
        insertNode(root.right , newVal)

insertNode(root , 7)
insertNode(root , 4)

preOrderTraversal(root)