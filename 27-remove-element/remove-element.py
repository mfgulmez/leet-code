class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        num_not_val = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                
            else:
                num_not_val += 1
                i += 1
        
        return num_not_val
        