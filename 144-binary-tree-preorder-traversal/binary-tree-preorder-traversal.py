# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preOrder(self, treeNode, result):
        if treeNode == None:
            return 
        
        result.append(treeNode.val)
        self.preOrder(treeNode.left, result)
        self.preOrder(treeNode.right, result)
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.preOrder(root, result)
        return result