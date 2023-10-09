from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
            Time Complexity: O(log(N))
            Space Complexity: O(1)
        """
        left = self.bin_search(nums, target, True)
        right = self.bin_search(nums, target, False)
        return [left, right]

    @staticmethod
    def bin_search(nums, target, left_bias):
        l, r = 0, len(nums) - 1
        i = - 1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if left_bias:
                    r = m - 1
                else:
                    l = m + 1
        return i


if __name__ == "__main__":
    print(Solution.searchRange(self=Solution, nums=[5, 7, 7, 8, 8, 10], target=8))
