from functools import reduce
from operator import xor
from typing import List


class Solution:
    @staticmethod
    def singleNumber(self, nums: List[int]) -> int:
        one = 0

        for num in nums:
            one = one ^ num

        return one

    @staticmethod
    def singleNumberSecond(self, nums: List[int]) -> int:
        return reduce(xor, nums)


if __name__ == "__main__":
    print(Solution.singleNumber(self=Solution, nums=[0, 1, 0, 1, 0, 1, 99]))
