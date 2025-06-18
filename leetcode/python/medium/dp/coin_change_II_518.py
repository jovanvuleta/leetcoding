from typing import List


class Solution:
    @staticmethod
    def change(amount: int, coins: List[int]) -> int:
        """
            Time complexity: O(amount * len(coins))
            Space complexity: O(amount)
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]

        return dp[amount]


if __name__ == "__main__":
    print(Solution.change(amount=5, coins=[1, 2, 5]))
