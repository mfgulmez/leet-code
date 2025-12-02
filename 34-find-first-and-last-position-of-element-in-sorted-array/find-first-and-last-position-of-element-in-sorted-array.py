class Solution(object):


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        low, high = 0, length - 1
        while low <= high:

            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                if nums[low] == target and nums[high] == target:
                    return [low, high]
              
                else:
                    if nums[low] < target:
                        low += 1
                    if nums[high] > target: 
                        high -= 1
        return [-1, -1]