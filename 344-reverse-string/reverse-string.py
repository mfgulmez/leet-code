class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        index = 0
        length = len(s) // 2
        for index in range(length):
            s[index] , s[len(s) - index - 1] = s[len(s) - index - 1], s[index]