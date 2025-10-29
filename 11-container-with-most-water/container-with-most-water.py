class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i != j:
            lower = min(height[i], height[j])
            area = lower * (j - i)
   
            if area > maxArea:
                maxArea = area

            if lower == height[i]:
                i += 1

            else:
                j -= 1
        return maxArea