class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        begin = False
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        first_letter = i
        while i < len(s) and s[i] != " ":
            i += 1
        return i - first_letter
        