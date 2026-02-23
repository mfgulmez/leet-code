class Solution(object):
    def binarySearch(self, low, high, nums, target):
        if low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                return self.binarySearch(low, mid - 1, nums, target)
            elif target > nums[mid]:
                return self.binarySearch(mid + 1, high, nums, target)
            else:
                return mid
        return -1
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(0, len(nums) - 1, nums, target)