class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_occurances, t_occurances = {}, {}
        index = 0
        while index < len(s):
            if s[index] not in s_occurances:
                s_occurances[s[index]] = 1
            else:
                s_occurances[s[index]] += 1
            index += 1
        index = 0
        while index < len(t):
            if t[index] not in t_occurances:
                t_occurances[t[index]] = 1
            else:
                t_occurances[t[index]] += 1
            index += 1
        
        return s_occurances == t_occurances
       