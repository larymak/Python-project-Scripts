# Binary tree implementation along with tree traversals

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Traverse pre-order
    def traversePreOrder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    
    # Traverse in-order
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.data, end=" ")
        if self.right:
            self.right.traverseInOrder()

    
    # Traverse post-order
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data, end=" ")


root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

print("Pre Order traversal: ", end=" ")
root.traversePreOrder()
print()
print("Post Order traversal: ",end=" ")
root.traversePostOrder()
print()
print("In Order traversal: ",end=" ")
root.traverseInOrder()
print()
