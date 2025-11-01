class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        i = len(digits) - 1
        extra = 1
        while i >= 0:
            total = digits[i] + extra
            digit = total % 10
            digits[i] = digit
            extra = int(total / 10)
            i -= 1
            if i == -1 and extra > 0:
                digits.insert(0, extra)
        return digits
        

        