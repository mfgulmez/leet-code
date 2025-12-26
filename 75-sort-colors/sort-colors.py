class Solution(object):
    def mergeSort(self, nums, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergeSort(nums, low, mid)
            self.mergeSort(nums, mid + 1, high)

            low_size = mid - low + 1
            high_size = high - mid
            low_array = [0] * low_size
            high_array = [0] * high_size
            
            for i in range(low_size):
                low_array[i] = nums[low + i]

            for i in range(high_size):
                high_array[i] = nums[mid + i + 1]

            low_index, high_index, nums_index = 0, 0, low
            while low_index < low_size and high_index < high_size:
                if low_array[low_index] <= high_array[high_index]:
                    nums[nums_index] = low_array[low_index]
                    low_index += 1
                else:
                    nums[nums_index] = high_array[high_index]
                    high_index += 1
                nums_index += 1
            
            while low_index < low_size:
                nums[nums_index] = low_array[low_index]
                low_index += 1
                nums_index += 1

            while high_index < high_size:
                nums[nums_index] = high_array[high_index]
                high_index += 1
                nums_index += 1




    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums, 0, len(nums) - 1)