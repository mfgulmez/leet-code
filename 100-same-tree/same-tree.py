# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrderComparison(self, p, q):
        if p is None and q is None:
            return False
        if p is None or q is None:
            return True   

        if self.inOrderComparison(p.left, q.left):
            return True 

        if p.val != q.val:
            return True   

        if self.inOrderComparison(p.right, q.right):
            return True   

        return False  



    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        return not self.inOrderComparison(p, q)
        