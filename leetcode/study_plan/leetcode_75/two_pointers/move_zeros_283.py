from typing import List


class Solution:

    @staticmethod
    def moveZeroes(self, nums: List[int]) -> None:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

    @staticmethod
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = nums.count(0)

        nums[:] = [num for num in nums if num != 0]
        nums += [0] * zeroes


if __name__ == "__main__":
    print(Solution.moveZeroes(self=Solution, nums=[0, 1, 0, 3, 12]))
