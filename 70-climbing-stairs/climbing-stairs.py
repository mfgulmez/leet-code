class Solution(object):
    def fibionacci(self, n, numbers):
        
        if n <= 2:
            if n not in numbers:
                numbers[n] = n
                return n
            else:
                return numbers[n]
        if n - 1 in numbers and n - 2 in numbers:
            return numbers[n - 1] + numbers[n - 2]
        else:
            numbers[n - 1] = self.fibionacci(n - 1, numbers)
            numbers[n - 2] = self.fibionacci(n - 2, numbers)
            return self.fibionacci(n - 1, numbers) + self.fibionacci(n - 2, numbers)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        numbers = {}
        return self.fibionacci(n, numbers)