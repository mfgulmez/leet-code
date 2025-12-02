class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]
        low, high = 0, length - 1
    
        while low < length and high > -1 and (nums[low] < target or nums[high] > target):
            if nums[low] < target:
                low += 1
            if nums[high] > target:
                high -= 1
        if low >= length or high < 0:
            return [-1, -1]
        if nums[low] == target or nums[high] == target:
            return [low, high]
        return [-1, -1]