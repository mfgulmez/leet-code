class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print(n & (n - 1))
        if n & (n - 1) == False and (n - 1) % 3 == 0:
            return True
        return False