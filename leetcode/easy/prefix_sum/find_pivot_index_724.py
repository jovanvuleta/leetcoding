from typing import List


class Solution:
    @staticmethod
    def pivotIndex(nums: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        start = 0
        remain = sum(nums)

        for i in range(len(nums)):
            remain -= nums[i]
            if remain == start:
                return i
            start += nums[i]

        return -1


if __name__ == "__main__":
    print(Solution.pivotIndex())
