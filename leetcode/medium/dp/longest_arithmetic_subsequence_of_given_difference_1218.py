from typing import List


class Solution:
    @staticmethod
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        dp, ans = {}, 0

        for num in arr:
            target = num - difference

            if target not in dp:
                dp[num] = 1
            else:
                dp[num] = 1 + dp[target]

            ans = max(ans, dp[num])

        return ans


if __name__ == "__main__":
    print(Solution.longestSubsequence(self=Solution, arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))
