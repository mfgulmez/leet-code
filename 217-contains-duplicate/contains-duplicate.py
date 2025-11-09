class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniques = set()
        index = 0
        while index < len(nums):
            if nums[index] not in uniques:
                uniques.add(nums[index])
            else:
                return True
            index += 1
        return False