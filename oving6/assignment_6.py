# -*- coding: utf-8 -*-
"""Assignment#6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IfPWONRwANaTJg6-M0yj6Z-UulMXTLbw
"""



"""# Assignment #6

# Complete the given python code. There are six parts to be done!
Please follow the comments in the code
"""



class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=' ')
		inorder(root.right)

# A utility function to insert a new node with given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)
	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node


def count_leaf_nodes():
   """ Let us take the following BST
      50
    / \
    30	 70
    / \ / \
  20 40 60 80

  Then it is expected to print 4 by calling the function
  """
		# write your code here




  # end

def preorder():
   """ Let us take following BST
      50
    / \
    30	 70
    / \ / \
  20 40 60 80

  Then it is expected to print 50,30,20,40,70,60,80 by calling the function
  """
	# write your code here




  # end

def print_nodes_with_two_child():

   """ Let us take following BST
      50
    / \
    30	 70
    / \ / \
  20 40 60 80

  Then it is expected to print 50,30,70 by calling the function
  """
	# write your code here




  # end



def print_nodes_bylevel():

   """ Let us take following BST
      50
    / \
    30	 70
    / \ / \
  20 40 60 80

  Then it is expected to print 50,30,70,20,40,60,80 by calling the function
  """
  # write your code here



  # end




def tree_height():
    # write your code here



  # end



# Driver Code
if __name__ == '__main__':


	#Q1:
  root = None

  # insert all nodes in the given order	by calling insert function
  nodes = [50,30,20,40,70,60,80,71,25,85]



	#Q2:
	print("\n tree_height:")

  #Q3:
	print("\n Number of leaf nodes:")

	#Q4:
  print("\n print nodes in level order:")


  #Q5:
	print("\n preorder traversal of tree:")


  #Q6:
	print("\n print_nodes_with_two_child:")