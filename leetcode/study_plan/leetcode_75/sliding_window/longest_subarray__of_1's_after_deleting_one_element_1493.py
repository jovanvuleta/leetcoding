from typing import List


class Solution:
    @staticmethod
    def longestSubarray(nums: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        l, r, count, k = 0, 0, 0, 1

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l


if __name__ == "__main__":
    result = Solution.longestSubarray(nums=[0,1,1,1,0,1,1,0,1])
