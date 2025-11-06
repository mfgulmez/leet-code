# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSums(self, treeNode, num, sums):
        if treeNode == None:
            return
        num += treeNode.val
        if treeNode.left == None and treeNode.right == None:
            sums.append(num)

        self.pathSums(treeNode.left, num, sums)
        self.pathSums(treeNode.right, num, sums)

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        sums = []
        self.pathSums(root, 0, sums)
        index = 0
        while index < len(sums):
            if sums[index] == targetSum:
                return True
            index += 1
        return False
