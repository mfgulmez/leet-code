class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        while True:
            while num >= 1:
                result += num % 10
                num /= 10
         
            if result / 10 < 1:
                return result
            num = result
            result = 0

