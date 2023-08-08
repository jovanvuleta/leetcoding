from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """
            Time complexity: O(log(N))
            Space complexity: O(1)
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # Left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # Right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


if __name__ == "__main__":
    print(Solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
