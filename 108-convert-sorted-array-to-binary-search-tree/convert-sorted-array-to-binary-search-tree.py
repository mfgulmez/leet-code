# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def construct_tree(self, low, high, nums):
        if low > high:
            return

        mid = (low + high) / 2
        root = TreeNode(nums[mid])

        root.left = self.construct_tree(low, mid - 1, nums)
        root.right = self.construct_tree(mid + 1, high, nums)
        return root

                
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.construct_tree(0, len(nums) - 1, nums)
        


        