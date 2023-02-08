class Tree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
	def addchild(self,data):
		if data == self.data:
			return
		if data <self.data:
			if self.left:
				self.left.addchild(data)
			else:
				self.left=Tree(data)
		else:
			if self.right:
				self.right.addchild(data)
			else:
				self.right=Tree(data)
	def inorder(self):
		elements=[]
		if self.left:
			elements+=self.left.inorder()
		elements.append(self.data)
		if self.right:
			elements+=self.right.inorder()
		return elements
	def


def buildTree(list1):
	root=Tree(list1[0])
	for i in range(1,len(list1)):
		root.addchild(list1[i])
	return root
if __name__ == '__main__':
	list1=[1,2,3,4,5]
	obj=buildTree(list1)
	print(obj.inorder())