class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = ""
        if x * -1 > 0:
            return False
        if (x / 10) < 1:
            return True
        temp_x = x
        while temp_x >= 1:
            reverse += str(temp_x % 10)
            temp_x /= 10
        reverse = int(reverse)
        if reverse < pow(-2, 31) or reverse > pow(2, 31):
            return False
        
        if reverse - x == 0:
            return True
        return False
