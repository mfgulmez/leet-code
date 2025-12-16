class Solution(object):
    def getMaxProfit(self, low, high, prices):
        if low == high:
            return prices[low], prices[low], 0

        mid = (low + high) // 2

        left_min, left_max, left_profit = self.getMaxProfit(low, mid, prices)
        right_min, right_max, right_profit = self.getMaxProfit(mid + 1, high, prices)

        cross_profit = right_max - left_min

        min_price = min(left_min, right_min)
        max_price = max(left_max, right_max)
        max_profit = max(left_profit, right_profit, cross_profit)

        return min_price, max_price, max_profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        return self.getMaxProfit(0, len(prices) - 1, prices)[2]