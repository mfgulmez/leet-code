class Solution(object):
    
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        length = len(s)
        num_checked = 0
        inv1, inv2 = 2 * numRows - 2, 0
        start = 0
        result = ""
        
        while num_checked < length:
            result += s[start]
            num_checked += 1
            index = start

            if inv1 != 0 and inv2 == 0:
                index += inv1
                while index < length:
                    print(s[index])
                    result += s[index]
                    num_checked += 1
                    index += inv1
                inv1 -= 2
                inv2 += 2

            elif inv1 == 0 and inv2 != 0:
                index += inv2
                while index < length:
                    print(s[index])
                    result += s[index]
                    num_checked += 1
                    index += inv2
                inv1 -= 2
                inv2 += 2

            else:
                while index < length:
                    index += inv1
                    if index < length:
                        result += s[index]
                        num_checked += 1
                        index += inv2
                        if index < length:
                            result += s[index]
                            num_checked += 1
                inv1 -= 2
                inv2 += 2
            start += 1
 
        return result

        