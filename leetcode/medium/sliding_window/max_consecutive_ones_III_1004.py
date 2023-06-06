from typing import List


class Solution:
    @staticmethod
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        l, r = 0, 0
        count = 0
        zero_count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            count = max(count, r - l + 1)

        return count

    @staticmethod
    def longestOnesAnotherSolution(self, nums: List[int], k: int) -> int:
        l = 0

        for r, n in enumerate(nums):
            k -= (1 - n)
            if k < 0:
                k += (1 - nums[l])
                l += 1

        return r - l + 1


if __name__ == "__main__":
    result = Solution.longestOnesAnotherSolution(self=Solution, nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=2)
    print(result)
