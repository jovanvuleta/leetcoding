from typing import List


class Solution:
    @staticmethod
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        buy = -prices[0]
        sell = 0

        for price in prices[1:]:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)

        return sell

    @staticmethod
    def maxProfitDpSolution(self, prices: List[int], fee: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]

        for i in range(1, n):
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)

        return sell[-1]


if __name__ == "__main__":
    print(Solution.maxProfit(self=Solution, prices=[1, 3, 2, 8, 4, 9], fee=2))
