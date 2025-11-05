# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def depth(self, treeNode):
        if treeNode == None:
            return 0
        depth_left = self.depth(treeNode.left)
        depth_right = self.depth(treeNode.right)

        return max(depth_left, depth_right) + 1
        
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        depth = self.depth(root)
        return depth
    
        