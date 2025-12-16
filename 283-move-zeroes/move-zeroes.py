class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index, count = 0, 0
        length = len(nums)
        initial_operator = 0
        while count < length:
            if nums[index] == 0:
                nums.pop(index)
                nums.insert(len(nums), 0)
            else:
                index += 1
            count += 1