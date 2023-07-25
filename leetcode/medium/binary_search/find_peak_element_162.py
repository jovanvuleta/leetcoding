from typing import List


class Solution:
    @staticmethod
    def findPeakElement(self, nums: List[int]) -> int:
        """
            Time complexity: O(log(N))
            Space complexity: O(N)
        """
        if len(nums) == 1:
            return 0

        l, r = 0, len(nums) - 1

        while l != r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1

        return l


if __name__ == "__main__":
    print(Solution.findPeakElement(self=Solution, nums=[1, 2, 1, 3, 5, 6, 4]))
