class Solution(object):
    def getMaxProfit(self, low, high, prices):
        if low + 1 < high:
            mid = (low + high) // 2
            lower_profit = prices[mid] - prices[low]
            upper_profit = prices[high] - prices[mid]
            min_lower, max_upper = min(prices[low:mid]), max(prices[mid:high + 1])
            intersect_profit  = max_upper - min_lower

            return max(intersect_profit, lower_profit, upper_profit, self.getMaxProfit(mid, high, prices), self.getMaxProfit(low, mid, prices))
        else:
            if low < high:
                print(prices[high] - prices[low])
                return prices[high] - prices[low]
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low, high = 0, len(prices) - 1
        maxProfit = self.getMaxProfit(low, high, prices)
        if maxProfit < 0:
            return 0
        return maxProfit