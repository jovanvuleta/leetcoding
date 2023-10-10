import sys
from bisect import bisect_right
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
            Time Complexity: O(n ∗ log(n))
            Space Complexity: O(n)
        """
        n = len(nums)
        nums = sorted(set(nums))
        ans = sys.maxsize

        for i, s in enumerate(nums):
            e = s + n - 1
            idx = bisect_right(nums, e)

            ans = min(ans, n - (idx - i))
        return ans


if __name__ == "__main__":
    print(Solution.minOperations(self=Solution, nums=[1, 2, 3, 5, 6]))
