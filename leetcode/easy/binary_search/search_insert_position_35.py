from typing import List


class Solution:
    @staticmethod
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
            Time complexity: O(log(N))
            Space complexity: O(1)
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 4
    print(Solution.searchInsert(self=Solution, nums=nums, target=target))
