class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        found = False
        found_index = -1
        haystack_index = 0
        needle_index = 0
        haystack_index_renewal = 0
        while haystack_index + needle_index < len(haystack) and found == False:
            if needle[needle_index] == haystack[haystack_index + needle_index]:
                if needle[0] == haystack[haystack_index + needle_index] and needle_index > 0 and haystack_index_renewal == 0:
                    haystack_index_renewal = haystack_index + needle_index
                needle_index += 1
                if needle_index == len(needle):
                    found_index = haystack_index
                    found = True
                    
            else:
                if haystack_index_renewal != 0:
                    haystack_index = haystack_index_renewal
                    haystack_index_renewal = 0
                elif needle_index != 0:
                    haystack_index += needle_index
                else:
                    haystack_index += 1
                needle_index = 0
            print(haystack_index, needle_index)
        return found_index
            