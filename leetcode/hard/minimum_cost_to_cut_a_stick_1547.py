import sys
from typing import List


class Solution:
    @staticmethod
    def minCost(self, n: int, cuts: List[int]) -> int:
        """
            Time complexity: O(N^3)
            Space complexity: O(N)
        """
        memo = {}

        def dp(start, end):
            if (start, end) in memo:
                return memo[(start, end)]

            ans = sys.maxsize
            can_cut = False

            for cut in cuts:
                if start < cut < end:
                    can_cut = True
                    ans = min(ans, dp(start, cut) + dp(cut, end) + end - start)

            if not can_cut:
                ans = 0

            memo[(start, end)] = ans
            return ans

        return dp(0, n)


if __name__ == "__main__":
    print(Solution.minCost(self=Solution, n=1, cuts=[2, 3, 5, 1, 3]))
