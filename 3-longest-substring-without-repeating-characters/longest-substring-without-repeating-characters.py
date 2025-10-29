class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0 or len(s) == 1):
            return len(s)

        max_length = 0
        i = 0
        j = 0
        unique_letters = {}
        while j < len(s):
            if s[j] in unique_letters:
                if (j - i) > max_length:
                    max_length = (j - i)
    
                i = unique_letters[s[j]] + 1
                j = i
                unique_letters = {}
            if s[j] not in unique_letters:
                unique_letters[s[j]] = j
                j += 1
            if j == len(s):
                if (j - i) > max_length:
                    max_length = (j - i)
                return max_length
        
            
            
                
            
        return max_length

                
         
        