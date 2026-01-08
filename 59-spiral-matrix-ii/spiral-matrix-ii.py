class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        count = 1
        corner = n - 1
        m_index, n_index = 0, 0
        length = n * n
        result = [[0]*n for _ in range(n)]
        direction = "R"
        while count <= length:
            result[m_index][n_index] = count
            print(corner)
            if direction == "R":
                if n_index == corner:
                    m_index = m_index + 1
                    direction = "D"
                else:
                    n_index += 1

            elif direction == "D":
                if m_index == corner:
                    n_index = n_index - 1
                    direction = "L"
                else:
                    m_index += 1

            elif direction == "L":
                if n_index == (n - corner - 1):
                    corner = corner - 1
                    m_index = m_index - 1
                    direction = "U"
                else:
                    n_index -= 1
            
            elif direction == "U":
                if m_index == (n - corner - 1):
                    n_index = n_index + 1
                    direction = "R"
                else:
                    m_index -= 1
            print(result, direction)
            count += 1
        return result