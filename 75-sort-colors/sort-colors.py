class Solution(object):
    def quickSort(self, nums, low, high):
        if low < high:
            i, j = low - 1, low
            pivot = nums[high]
            while j < high:
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            self.quickSort(nums, low, i)
            self.quickSort(nums, i + 2, high)

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.quickSort(nums, 0, len(nums) - 1)