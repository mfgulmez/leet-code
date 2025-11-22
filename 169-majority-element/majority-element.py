class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low, high, n = 0, len(nums) - 1, len(nums)
        occurances = {}
       
        while high - low >= 0:
            low_num = nums[low]
            high_num = nums[high]

            if low_num in occurances:
                occurances[low_num] += 1
                if occurances[low_num] >= n // 2:
                    return low_num
            else:
                occurances[low_num] = 0
            
            if high_num in occurances:
                occurances[high_num] += 1
                if occurances[high_num] >= n // 2:
                    return high_num
            else:
                occurances[high_num] = 0
            low += 1
            high -= 1

