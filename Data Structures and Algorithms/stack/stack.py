class stack:

	def __init__(self):
		self.items=input()
		print(self.items.lstrip)

	def is_empty(self):
		return self.items==[]

	def push(self,item):
		self.items.insert(0,item)

	def pop(self):
		return self.items.pop(0)

	def print_stack(self):
		print(self.items)

stack1=stack()
stack1.push(5) #allows the user to add items to the stack
stack1.pop() #allows one to remove items to the stack
stack1.print_stack()

# stack implemetation using linkedlist

# Create a class for Node that represents an individual element of the linked list
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinked:
    def __init__(self):
        self.start = None

    # Method to add a new element to the top of the stack
    def push(self, data):
        newNode = Node(data)

        # If the stack is empty, make the new node the first element
        if(self.start == None):
            self.start = newNode
        else:

            # If the stack already has elements, add the new node to the top of the stack
            newNode.next = self.start
            self.start = newNode

        # Method to remove the top element from the stack
    def pop(self):
        if self.start is not None:
            self.start = self.start.next

        # Method to get the top element of the stack
    def top(self):
        return self.start

        # Method to check if the stack is empty
    def isEmpty(self):
        return self.start == None

        # Method to check if the stack is full
    def isFull(self):
        newNode = Node(None)
        return newNode == None


S = StackLinked()

S.push(45)
S.push(90)
S.push(12)
S.pop()
print(S.isEmpty())
print(S.isFull())
top_element = S.top()
print(top_element.data)



	


