class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        start, end = 0, len(s) - 1
        while start < end:
            start_letter = s[start].lower()
            end_letter = s[end].lower()
            start_is_vowel = (start_letter == "a" or start_letter == "e" or
                                start_letter == "i" or start_letter == "o" or start_letter == "u")
            end_is_vowel = (end_letter == "a" or end_letter == "e" or
                                end_letter == "i" or end_letter == "o" or end_letter == "u")
            if start_is_vowel and end_is_vowel:
                s = s[:start] + s[end] + s[start + 1: end] + s[start] + s[end + 1:]
                start += 1
                end -= 1
            elif start_is_vowel:
                end -= 1
            elif end_is_vowel:
                start += 1
            else:
                start += 1
                end -= 1       
        return s