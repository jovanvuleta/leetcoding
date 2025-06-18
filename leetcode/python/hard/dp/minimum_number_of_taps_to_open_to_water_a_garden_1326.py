from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
            Intuition: DP
            Time complexity: O(N^2) - For each tap, we potentially update O(N) elements in the DP array.
            Space complexity: O(N) - dp array storing
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i, r in enumerate(ranges):
            start, end = max(0, i - r), min(n, i + r)
            for j in range(start + 1, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
