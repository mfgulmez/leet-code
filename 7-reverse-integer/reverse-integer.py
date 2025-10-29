class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        while x % 10 == 0:
            x /= 10
        
        result = 0
        num_list = []
        negative = False
        if (x / -1) > 0:
            negative = True
        
        if negative:
            x *= -1
            while x >= 1:
                num_list.append(x % 10)
                x /= 10

            for i in range(0, len(num_list)):
                result += num_list[i] * pow(10, len(num_list) - i - 1)
            result *= -1

            if result < pow(-2, 31):
                return 0
            return result
        else:
            while x >= 1:
                num_list.append(x % 10)
                x /= 10
                
            for i in range(0, len(num_list)):
                result += num_list[i] * pow(10, len(num_list) - i - 1)

            if result > (pow(2, 31) - 1):
                return 0
            return result
