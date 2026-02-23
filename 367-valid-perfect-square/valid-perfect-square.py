class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        root = 1
        if num % 2 == 0:
            root = 2
        while root * root < num:
            root += 2
        if root * root == num:
            return True
        return False