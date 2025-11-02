class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]
        b = b[::-1]

        length, index = max(len(a), len(b)), 0
        bin_extra = 0
        result = ""
        while index < length:
            if index < len(a) and index < len(b):
                bin_dig = (int(a[index]) ^ int(b[index])) ^ bin_extra
                if(int(a[index]) + int(b[index]) + bin_extra >= 2):
                    bin_extra = 1
            
                else:
                    bin_extra = 0
                
                result = str(bin_dig) + result

            elif index < len(a):
                bin_dig = int(a[index]) ^ bin_extra
                bin_extra = int(a[index]) & bin_extra
                result = str(bin_dig) + result
            
            elif index < len(b):
                bin_dig = int(b[index]) ^ bin_extra
                bin_extra = int(b[index]) & bin_extra
                result = str(bin_dig) + result
            
            index += 1
            if index >= length and bin_extra > 0:
                result = str(bin_extra) + result

        return result
