class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        count = 0
        m, n = len(matrix), len(matrix[0])
        m_index, n_index = 0, 0
        length = len(matrix) * len(matrix[0])
        result = []
        direction = "R"
        while count < length:

            result.append(matrix[m_index][n_index])
            if direction == "R":
                if n_index == (n - 1):
                    m_index = m_index + 1
                    direction = "D"
                else:
                    n_index += 1

            elif direction == "D":
                if m_index == (m - 1):
                    m = m - 1
                    n_index = n_index - 1
                    direction = "L"
                else:
                    m_index += 1

            elif direction == "L":
                if n_index == len(matrix[0]) - n:
                    n = n - 1
                    m_index = m_index - 1
                    direction = "U"
                else:
                    n_index -= 1
            
            elif direction == "U":
                if m_index == len(matrix) - m:
                    n_index = n_index + 1
                    direction = "R"
                else:
                    m_index -= 1
            
            count += 1
        return result