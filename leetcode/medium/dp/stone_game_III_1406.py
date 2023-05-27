import sys
from typing import List


class Solution:
    @staticmethod
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
            Time complexity: O(N * k)
            Space complexity: O(N)
        """
        n = len(stoneValue)

        dp = [-sys.maxsize] * n

        for i in range(n - 1, -1, -1):
            for k in (1, 2, 3):
                dp[i] = max(dp[i], sum(stoneValue[i: i + k]) - (dp[i + k] if i < n - k else 0))

        return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"


if __name__ == "__main__":
    print(Solution.stoneGameIII(self=Solution, stoneValue=[1, 2, 3, 7]))
