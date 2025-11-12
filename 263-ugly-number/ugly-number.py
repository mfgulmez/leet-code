class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n % 2 == 0:
            while n % 2 == 0:
                n /= 2
        if n % 3 == 0:
            while n % 3 == 0:
                n /= 3
        if n % 5 == 0:
            while n % 5 == 0:
                n /= 5
        return n == 1
        
