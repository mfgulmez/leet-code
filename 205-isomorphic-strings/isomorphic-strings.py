class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        t_mapping = {}
        s_mapping = {}
        while index < len(s):
            t_char, s_char = s[index], t[index]
            if t_char in t_mapping:
                if s_char != t_mapping[t_char]:
                    return False
            elif s_char in s_mapping:
                if t_char != s_mapping[s_char]:
                    return False          
            else:
                t_mapping[t_char] = s_char
                s_mapping[s_char] = t_char
            index += 1
        return True
