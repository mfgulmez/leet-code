class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0, numRows):
            row = []
            if i > 1:
                row += [1]
                previous_row = result[i - 1]
                j = 0
                while j < i - 1:
                    row += [previous_row[j] + previous_row[j + 1]]
                    j += 1
                row += [1]
            elif i == 1:
                row = [1, 1]
            else:
                row = [1]
            result.append(row)
        return result
            
        