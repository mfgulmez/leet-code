import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        result = ""
        for i in s:
            if i >= "0" and i <= "9" or i >= "a" and i <= "z":
                result += i.lower()
        isPalindrome = True
        i = 0
        while isPalindrome and i < len(result) / 2:
            if result[i] != result[len(result) - i - 1]:
                isPalindrome = False
            i += 1
        return isPalindrome

        
        