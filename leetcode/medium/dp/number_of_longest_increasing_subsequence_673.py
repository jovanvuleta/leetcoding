from typing import List


class Solution:
    @staticmethod
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(N)
        """
        dp = [1] * len(nums)
        count = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:  # new max is here, never seen it before
                        dp[i] = dp[j] + 1  # set the max length
                        count[i] = count[j]  # set the initial value for count
                    elif dp[j] + 1 == dp[i]:  # we've seen this before if their equal
                        count[i] += count[j]  # increment the count

        longest_len = max(dp)

        return sum([count[i] for i in range(len(nums)) if dp[i] == longest_len])


if __name__ == "__main__":
    print(Solution.findNumberOfLIS(self=Solution, nums=[1, 3, 5, 4, 7]))
