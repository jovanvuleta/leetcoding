import math
from typing import List


class Solution:
    @staticmethod
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            Time complexity: O(N * log(U))
            Space complexity: O(1)
        """

        def helper(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        l, r = 1, max(piles)
        min_speed = -1

        while l <= r:
            m = (l + r) // 2
            if helper(m):
                min_speed = m
                r = m - 1
            else:
                l = m + 1
        return min_speed


if __name__ == "__main__":
    print(Solution.minEatingSpeed(self=Solution, piles=[3, 6, 7, 11], h=8))
