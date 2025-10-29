class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s[0]
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            return s[0]
        
        maxLength = 0
        result = ""
        for i in range(1, len(s) - 1):
            down = i
            up = i

            while (down - 1) >= 0 and s[down - 1] == s[i]:
                down -= 1

            while (up + 1) < len(s) and s[up + 1] == s[i]:
                up += 1

            palindrome = True
            while (down - 1) >= 0 and (up + 1) < len(s) and palindrome:
                if s[down - 1] != s[up + 1]:
                    palindrome = False
                else:
                    up += 1
                    down -= 1
                

            candidate = s[down:up + 1]
            if len(candidate) > maxLength:
                maxLength = len(candidate)
                result = candidate
        return result