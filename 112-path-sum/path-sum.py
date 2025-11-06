# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSums(self, treeNode, num, targetSum):
        if treeNode == None:
            return False
            
        num += treeNode.val
        if treeNode.left == None and treeNode.right == None:
            return num == targetSum

        return self.pathSums(treeNode.left, num, targetSum) or self.pathSums(treeNode.right, num, targetSum)

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        return self.pathSums(root, 0, targetSum)
     
