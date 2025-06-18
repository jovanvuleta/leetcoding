from typing import List


class Solution:
    @staticmethod
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(N*M)
        """
        dp = [{} for _ in range(len(nums))]

        ans = 0

        for i in range(len(nums)):
            dp[i][0] = 1
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1

            ans = max(ans, max(dp[i].values()))

        return ans


if __name__ == "__main__":
    print(Solution.longestArithSeqLength(self=Solution, nums=[9, 4, 7, 2, 10]))
