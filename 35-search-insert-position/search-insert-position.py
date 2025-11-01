class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low, high = 0, len(nums) - 1
        center = 0
        while (high >= low):
            center = int((low + high)/2)

            if target == nums[center]:
                return center

            elif high == low:
                if target > nums[center]:
                    return center + 1
                elif target < nums[center]:
                    return center
                
            elif target > nums[center]:
                low = center + 1

            elif target < nums[center]:
                high = center - 1
    

        return center