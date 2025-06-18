from typing import List


class Solution:
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        seen = 0
        for num in nums:
            if seen & (1 << num):
                return num
            seen |= 1 << num


if __name__ == "__main__":
    print(Solution.findDuplicate(nums=[3, 1, 3, 4, 2]))
