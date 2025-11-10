class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        
        while n >= 1:
            if n % 2 == 1:
                result += 1
            n /= 2
        return result