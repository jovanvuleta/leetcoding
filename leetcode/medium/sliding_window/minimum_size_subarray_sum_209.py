from typing import List


class Solution:
    @staticmethod
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        l = r = total = 0
        mn = float('inf')

        while r < len(nums):
            total += nums[r]

            while total >= target:
                mn = min(mn, r - l + 1)
                total -= nums[l]
                l += 1

            r += 1

        return 0 if mn == float('inf') else mn

    def minSubArrayLenWithForLoop(self, target: int, nums: List[int]) -> int:
        l = r = total = 0
        mn = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                mn = min(mn, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if mn == float('inf') else mn


if __name__ == "__main__":
    print(Solution.minSubArrayLen(self=Solution, nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], target=3))
