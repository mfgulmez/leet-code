# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postOrder(self, treeNode, result):
        if treeNode == None:
            return
        self.postOrder(treeNode.left, result)
        self.postOrder(treeNode.right, result)
        result.append(treeNode.val)

    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.postOrder(root, result)
        return result