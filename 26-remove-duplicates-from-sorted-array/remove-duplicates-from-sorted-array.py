class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniques = []
        i = 0
        while i < len(nums):
            if nums[i] in uniques:
                del nums[i]
            else:
                uniques.append(nums[i])
                i += 1
        print(nums)
        return len(nums)