class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif n >= 1:
            while n > 1:
                if n % 3 != 0:
                    return False
                n /= 3
            return True

        elif n > 0:
            n = 1 // n
            while n > 1:
                if n % 3 != 0:
                    return False
                n /= 3
            return True
        else:
            return False
        