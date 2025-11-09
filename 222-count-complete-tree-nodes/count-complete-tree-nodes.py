# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def numberOfNodes(self, treeNode):
        if treeNode == None:
            return 0
        elif treeNode.left == None and treeNode.right == None:
            return 1
       
        return self.numberOfNodes(treeNode.left) + self.numberOfNodes(treeNode.right) + 1

    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        return self.numberOfNodes(root)
   