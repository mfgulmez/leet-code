class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sum_range = (length) * (length + 1) / 2
        return sum_range - sum(nums)