class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        low, high = 0, length - 1

        while low < length and high > -1:
            
            if (nums[low] == target and nums[high] <= target 
                or nums[high] == target and nums[low] >= target):
                return [low, high]
            elif low > high:
                return [-1, -1]
            if nums[low] < target:
                low += 1
            if nums[high] > target:
                high -= 1
        
        return [-1, -1]