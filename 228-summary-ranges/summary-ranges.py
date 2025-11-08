class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        index = 0
        while index < len(nums):
            start = index < len(nums) and nums[index]
            if nums[index] - start > 1:
                index += 1
            else:
                end = start
                while index < len(nums) and nums[index] - end <= 1:
                    end = nums[index]
                    index += 1
            if start != end:
                result.append(str(start) + "->" + str(end))
            else:
                result.append(str(start))
        return result