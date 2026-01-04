class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        uniques1, uniques2 = list(set(nums1)), list(set(nums2))
        for i in uniques1:
            if i in uniques2:
                result.append(i)
        return result