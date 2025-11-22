class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result, iterator = 0, 31
        while n >= 1:
            result += pow(2, iterator) * (n % 2)
            iterator -= 1
            n //= 2

        return result