#yor are given a binary  tree .return the count of unival sub-trees in the given binary tree. in unival trees, all nodes below the rootnode.have the same same valueas the data of the root#  
'''
	Time Complexity: O(N^2)
	Space Complexity: O(N)
    
	Where N is the total number of nodes in the given Binary Tree. 
'''


import queue
import sys
sys.setrecursionlimit(10**6)

class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None




def isUnivalTree(root, data):
    
    if root == None:
        return True
    
    if root.data == data:
        
        return isUnivalTree(root.left, data) and isUnivalTree(root.right, data)
    
    return False

def countUnivalTrees(root):
    
    if root == None:
        return 0
    
    countLeft = countUnivalTrees(root.left)
    countRight = countUnivalTrees(root.right)
    
    count = countLeft + countRight
    
    if (isUnivalTree(root, root.data)):
        count += 1
        
    return count


def buildLevelTree(levelorder):
    
    index = 0
    length = len(levelorder)
    
    if length<=0 or levelorder[0]==-1:
        return None
    
    
    root = BinaryTreeNode(levelorder[index])
    index += 1
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        
        if leftChild != -1:
            
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
            
        rightChild = levelorder[index]
        index += 1
        
        
        if rightChild != -1:
            
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
            
    return root
    
t = int(input())

while t >0:
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(countUnivalTrees(root))
    t = t -1




