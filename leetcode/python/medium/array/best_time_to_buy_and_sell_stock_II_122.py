class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit += diff
        return profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        hi = lo = prices[0]
        profit = 0
        n = len(prices)

        while i < n - 1:
            while i < n - 1 and prices[i] > prices[i + 1]:
                i += 1
            lo = prices[i]

            while i < n - 1 and prices[i] < prices[i + 1]:
                i += 1
            hi = prices[i]
            profit += hi - lo

        return profit
