class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sums = []
        cycle = False

        while True:
            square_sum = 0
            while n >= 1:
                square_sum += pow(n % 10, 2)
                n /= 10
            if square_sum == 1:
                return True
            elif square_sum in sums:
                return False
            else:
                sums.append(square_sum)
                n = square_sum
                
