class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None
class Doubly:
	def __init__(self):
		self.head=None
	def push(self,data):
		newnode=Node(data)
		newnode.next=self.head
		if self.head is not None:
			self.head.prev=newnode
		self.head=newnode
	def printlist(self):
		printval=self.head
		while printval:
			print(printval.data)
			printval=printval.next
	def insertnode(self,prev_node,newval):
		if prev_node is None:
			return
		newnode=Node(newval)
		newnode.next=prev_node.next
		newnode.prev=prev_node
		if newnode.next is not None:
			newnode.next.prev=newnode
		

if __name__ == '__main__':
	list1=Doubly()
	list1.push("mon")
	list1.push("tue")
	list1.push("thur")
	list1.push("fri")
	list1.insertnode(list1.head.next,"wed")
	list1.printlist()