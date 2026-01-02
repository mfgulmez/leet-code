class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        index = 0
        while index < (len(s) // 2):
            s[index] , s[len(s) - index - 1] = s[len(s) - index - 1], s[index]
            index += 1