# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def numberOfNodes(self, treeNode, result):
        if treeNode == None:
            return
       
        self.numberOfNodes(treeNode.left, result)
        result.append(0)
        self.numberOfNodes(treeNode.right, result)
    
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = []
        self.numberOfNodes(root, result)
        return len(result)