class Solution(object):
    def recursivePow(self, x, n):
        if n == 1:
            return x
      
        base = self.recursivePow(x, n // 2)
        result = base * base
        if n % 2 == 0:
            return result
        else:
            return result * x
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        negative_power = False
        if n < 0:
            negative_power = True
        elif n == 0:
            return 1
    
        result = 1
        if negative_power == False:
            result = self.recursivePow(x, n)
            return result

        else:
            n *= -1
            result = self.recursivePow(x, n)
            result = 1 / result
            return result
