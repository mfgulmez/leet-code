class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        lenSum = len1 + len2

        odd1 = False if len1 % 2 == 0 else True
        odd2 = False if len2 % 2 == 0 else True
        oddSum = False if lenSum % 2 == 0 else True

        if len1 == 0:
            if len2 == 1:
                return nums2[0]
            elif odd2:
                return nums2[int(len2 / 2)]
            return (nums2[len2 / 2] + nums2[(len2 / 2) - 1]) / 2.0

        elif len2 == 0:
            if len1 == 1:
                return nums1[0]
            elif odd1:
                return nums1[int(len1 / 2)]
            return (nums1[len1 / 2] + nums1[(len1 / 2) - 1]) / 2.0

        elif nums2[0] >= nums1[len1 - 1]:
            nums = nums1 + nums2
            if(oddSum):
                return nums[int(lenSum / 2)]
            return (nums[lenSum / 2] + nums[(lenSum / 2) - 1]) / 2.0

        elif nums1[0] >= nums2[len2 - 1] :
            nums = nums2 + nums1
            if(oddSum):
                return nums[int(lenSum / 2)]
            return (nums[lenSum / 2] + nums[(lenSum / 2) - 1]) / 2.0

        nums = nums1 + nums2
        nums.sort()
        if(oddSum):
            return nums[int(lenSum / 2)]
        return (nums[lenSum / 2] + nums[(lenSum / 2) - 1]) / 2.0
        
        return 0 