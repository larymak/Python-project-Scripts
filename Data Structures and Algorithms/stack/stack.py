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
stack1.push(5)
stack1.pop()
stack1.print_stack()


	

