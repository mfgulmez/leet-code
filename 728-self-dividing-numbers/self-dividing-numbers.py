class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        index = left
        self_dividing_nums = []
        while index <= right:
            divisable = 0
            num_digits = 0
            num = index
            while index >= 1:
                num_digits += 1
                digit = index % 10
                if digit == 0:
                    break
                if num % digit == 0:
                    divisable += 1
                index = (index - digit) / 10
    
            if num_digits == divisable:
                self_dividing_nums.append(num)

            index = num + 1
        return self_dividing_nums