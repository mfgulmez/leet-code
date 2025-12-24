class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)
        
        capacity.sort()
        capacity.reverse()
        count, index = 0, 0
        while total_apples > 0:
            total_apples -= capacity[index]
            count += 1
            index += 1
        return count
