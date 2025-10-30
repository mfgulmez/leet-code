class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        initial = needle[0]
        found = False
        found_index = -1
        haystack_index = 0
        while haystack_index < len(haystack) and found == False:
            needle_index = 0
            
            while needle_index < len(needle) and (haystack_index + needle_index) < len(haystack):
                if(needle[needle_index] != haystack[haystack_index + needle_index]):
                    needle_index = len(needle) + 1
                
                else:
                    needle_index += 1
                
            if needle_index == len(needle):
                found = True
                found_index = haystack_index
                haystack_index = len(haystack)
            else:
                haystack_index += 1
                while haystack_index < len(haystack) and haystack[haystack_index] != initial:
                    haystack_index += 1
            print(haystack_index)
        return found_index


            