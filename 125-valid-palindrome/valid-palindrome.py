import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        result = "".join(re.findall("[a-z]|[0-9]", s.lower()))
        isPalindrome = True
        i = 0
        while isPalindrome == True and i < len(result) / 2:
            if result[i] != result[len(result) - i - 1]:
                isPalindrome = False
            i += 1
        return isPalindrome

        
        