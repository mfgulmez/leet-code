class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        pow_index = 0
        result = 0
        for char in columnTitle:
            result += (ord(char) - 64) * pow(26, len(columnTitle) - pow_index - 1)
            pow_index += 1
        return result