from typing import List


class Solution:
    @staticmethod
    def maxProfit(self, prices: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        profit = 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]

        return profit


if __name__ == "__main__":
    print(Solution.maxProfit(self=Solution, prices=[7, 1, 5, 3, 6, 4]))
