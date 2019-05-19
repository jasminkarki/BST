from bst import BST 
import unittest

class BSTTestCase(unittest.TestCase):

	def test_bstTest(self):
		bst=BST()

		#Test Case for add
		bst.add(10,"Value for A")
		# self.assertEqual(bst.size(),1) 		#Check for size. TRUE

		bst.add(5,"Value for B")
		# self.assertEqual(bst.size(),2)		#Check for size. TRUE

		bst.add(15,"Value for C")
		# self.assertEqual(bst.size(),3)		#Check for size. TRUE

		# self.assertListEqual(bst.in_order(),[5,10,15])	

		bst.add(11,"Value for D")			#Add value to check Traversal
		bst.add(20,"Value for E")			#Add value to check Traversal


		#Inorder,Preorder and Postorder
		self.assertListEqual(bst.in_order(),[5,10,11,15,20])
		self.assertListEqual(bst.post_order(),[5,11,20,15,10])
		self.assertListEqual(bst.pre_order(),[10,5,15,11,20])

		#Search Element
		self.assertEqual(bst.search(5),[1])
		
		#Largest and Smallest Check
		self.assertListEqual(bst.findSmallestKey(),[5])
		self.assertListEqual(bst.findLargestKey(),[20])


if __name__=="__main__":
	unittest.main()