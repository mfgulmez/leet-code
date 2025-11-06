class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        result.append(1)
        denominator = 1
        while denominator <= rowIndex:
            result.append(result[len(result) - 1] * (rowIndex + 1 - denominator) / denominator)
            denominator += 1
        return result
            
        