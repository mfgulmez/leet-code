class Solution(object):
    def recursivePow(self, x, n):
        print(x, n)
        if n == 1:
            return x
        elif n == 2:
            return x * x
        base = self.recursivePow(x, n // 2)
        if n % 2 == 0:
            return base * base
        else:
            return base * self.recursivePow(x, n - (n // 2))
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
      
        power_decimal_part = n // 1
        power_ratio_part = n % 1
        result = 1
        if negative_power == False:
 
            result = self.recursivePow(x, n)
            return result
        else:
            n *= -1
            result = self.recursivePow(x, n)
            result = 1 / result
            return result
