# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def getInvertedTree(self, treeNode):
        if treeNode != None:
            tempNode = treeNode.left
            treeNode.left = treeNode.right
            treeNode.right = tempNode
            self.getInvertedTree(treeNode.left)
            self.getInvertedTree(treeNode.right)
     
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.getInvertedTree(root)
        return root