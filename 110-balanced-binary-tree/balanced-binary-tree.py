# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def depth_comparison(self, treeNode):
        if treeNode == None:
            return -1, True
        depth_left, left_balanced = self.depth_comparison(treeNode.left)
        depth_right, right_balanced = self.depth_comparison(treeNode.right)
        
        return (max(depth_left, depth_right) + 1, abs(depth_left - depth_right) <= 1 and left_balanced and right_balanced)
        
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        

            
        return self.depth_comparison(root)[1]