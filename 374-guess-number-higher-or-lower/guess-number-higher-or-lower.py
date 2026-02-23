# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        guess_diff = guess(n)
        temp_n = n // 2
        while guess_diff != 0:
            if guess_diff == 1:
                n = n + abs(temp_n - n) // 2
            elif guess_diff == -1:
                temp_n = n
                n //= 2
                
            guess_diff = guess(n)
        return n