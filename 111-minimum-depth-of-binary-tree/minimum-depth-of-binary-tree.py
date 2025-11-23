# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimum_depth(self, treeNode):
        if treeNode == None:
            return 0

        depth_left = self.minimum_depth(treeNode.left)
        depth_right = self.minimum_depth(treeNode.right)

        min_depth = min(depth_left, depth_right) + 1

        if min_depth > 1:
            return min_depth
        return max(depth_left, depth_right) + 1

    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
      
        return self.minimum_depth(root)
          
        return 0
         
        