class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        initial = strs[0]
        common = True
        result = ""
        i = 1
        while common and i < (len(initial) + 1):
            j = 1
            while j < len(strs) and common:
                if initial[0:i] != strs[j][0:i]:
                    common = False
                j += 1
            if common:
                print(result)
                result = initial[0:i]
            i += 1
        return result