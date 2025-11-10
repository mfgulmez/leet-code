class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_decimal = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        result = 0
        index = len(s) - 1
        while index >= 0:
            
            current_roman = roman_to_decimal[s[index]]
            if index - 1 >= 0:
                next_roman = roman_to_decimal[s[index - 1]]
                if current_roman > next_roman:
                    result += current_roman - next_roman
                    index -= 2
                else:
                    result += current_roman
                    index -= 1

            else:
                result += current_roman
                index -= 1
    
            
        return result