from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def singleNumber(self, nums: List[int]) -> int:
        """
            Intuition: Bit manipulation
            Time complexity: O(N)
            Space complexity: O(1)
        """
        one, two = 0, 0

        for x in nums:
            two = two ^ (one & x)  # counts number that appeared twice
            one = one ^ x  # counts number that appeared once
            not_three = ~(two & one)  # mask that set bits to 0 for numbers that appeared 3 times

            one, two = not_three & one, not_three & two  # resetting bits to 0 if appeared 3 times

        return one


if __name__ == "__main__":
    print(Solution.singleNumber(self=Solution, nums=[0, 1, 0, 1, 0, 1, 99]))
