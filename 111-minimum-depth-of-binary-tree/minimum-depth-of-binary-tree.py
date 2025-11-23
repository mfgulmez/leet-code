# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimum_depth(self, treeNode):
        if treeNode is None:
            return 0

        if not treeNode.left and not treeNode.right:
            return 1

        if not treeNode.left:
            return 1 + self.minDepth(treeNode.right)
        if not treeNode.right:
            return 1 + self.minDepth(treeNode.left)

        return 1 + min(self.minDepth(treeNode.left), self.minDepth(treeNode.right))

    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
      
        return self.minimum_depth(root)
     
         
        