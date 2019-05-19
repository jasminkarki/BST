# from time import time

class BST:
	def __init__(self):
		self._size=0
		self._root=None

	class BSTNode:
		def __init__(self,key,value):
			self.key=key
			self.value=value
			self.left=None
			self.right=None
			# self.name=None
			# self.roll=None
			# self.add=None

	def add(self,key,value):
		z=self.BSTNode(key,value)
		y=None
		x=self._root
		while(x!=None):
			y=x
			if (key<x.key):
				x=x.left
			else:
				x=x.right
		if(y==None):
			self._root=z
		elif(z.key<y.key):
			y.left=z
		else:
			y.right=z
		self._size+=1


	def is_empty(self):
		return self._size==0

	def size(self):
		return self._size


	def in_order(self):			#Left Root Right
		nodes=[]
		self._in_order(self._root,nodes)
		return nodes

	def _in_order(self, subtree, nodes):
		if subtree:
			self._in_order(subtree.left,nodes)
			nodes.append(subtree.key)
			self._in_order(subtree.right,nodes)

	def pre_order(self):		#Root Left Right
		nodes=[]
		self._pre_order(self._root,nodes)
		return nodes

	def _pre_order(self, subtree, nodes):
		if subtree:
			nodes.append(subtree.key)
			self._pre_order(subtree.left,nodes)
			self._pre_order(subtree.right,nodes)


	def post_order(self):		#Left Right Root
		nodes=[]
		self._post_order(self._root,nodes)
		return nodes

	def _post_order(self, subtree, nodes):
		if subtree:
			self._post_order(subtree.left,nodes)
			self._post_order(subtree.right,nodes)
			nodes.append(subtree.key)	

	def search(self,key):
		found=[]
		self._search(self._root,key,found)


	def _search(self,subtree,key,found):
		if (subtree):
			if(key==subtree.key):
				found.append(1)
			elif(key<subtree.key):
				self._search(subtree.left,key,found)
			elif(key>subtree.key):
				self._search(subtree.right,key,found)

	def findSmallestKey(self):
		nodes = []
		self._findSmallestKey(self._root, nodes)
		return nodes

	def _findSmallestKey(self, subtree, nodes):
		if(subtree):
			if(subtree.left == None):
				nodes.append(subtree.key)
			self._findSmallestKey(subtree.left, nodes)

	def findLargestKey(self):
		nodes = []
		self._findLargestKey(self._root, nodes)
		return nodes

	def _findLargestKey(self, subtree, nodes):
		if(subtree):
			if(subtree.right == None):
				nodes.append(subtree.key)
			self._findLargestKey(subtree.right, nodes)



'''
# arr=[]
# arr=[0]*11
# i=0
# arr[i]=time()
# i+=1
# print (arr[i])
'''