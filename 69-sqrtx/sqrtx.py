class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low, high = 0, x
        while(high >= low):
            center = int((high + low) / 2)
            print(low, high, center)
            if center * center == x:
                return center
            elif low * low == x:
                return low
            elif high * high == x:
                return high
            elif high - low == 1:
                return low
            elif center * center < x:
                low = center
            elif center * center > x:
                high = center
       

    