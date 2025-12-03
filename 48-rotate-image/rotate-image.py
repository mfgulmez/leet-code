class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i = 0
        length = len(matrix)
        while i < length // 2:
            j, column_length = i, len(matrix[i])
    
            while j < length - i - 1:
                temp = matrix[column_length - j - 1][i]    

                matrix[length - j - 1][i] = matrix[length - i - 1][length - j - 1]
                matrix[length - i - 1][length - j - 1] = matrix[j][length - i - 1]
                matrix[j][length - i - 1] = matrix[i][j]
                matrix[i][j] = temp
                j += 1
            i += 1
        