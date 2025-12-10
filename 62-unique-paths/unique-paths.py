class Solution(object):
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
      
        return n * factorial(n - 1)

    def combination(self, n, r):
        return self.factorial(n) / (self.factorial(n - r) * self.factorial(r))

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            return self.combination(m + n - 2, n - 1)
        return self.combination(m + n - 2, m - 1)