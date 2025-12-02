class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        low, high = 0, length - 1

        while low < length and nums[low] < target:
            low += 1
        while high > -1 and nums[high] > target:
            high -= 1
        if low > high:
            return [-1, -1]
        return [low, high]