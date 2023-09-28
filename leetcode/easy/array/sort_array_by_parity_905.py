from typing import List


class Solution:
    @staticmethod
    def sortArrayByParity(nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]


if __name__ == "__main__":
    print(Solution.sortArrayByParity(nums=[3, 1, 2, 4]))
