import math
from typing import List


class Solution:
    @staticmethod
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        """
            Time complexity: O(N * log(U))
            Space complexity: O(N)
        """

        def can_reach(speed):
            so_far = 0
            for d in dist[:-1]:
                so_far += math.ceil(d / speed)
                if so_far > hour:
                    return False
            return (so_far + (dist[-1] / speed)) <= hour

        l = 1
        r = 10 ** 7
        min_speed = -1

        while l <= r:
            m = (l + r) // 2
            if can_reach(m):
                min_speed = m
                r = m - 1
            else:
                l = m + 1
        return min_speed


if __name__ == "__main__":
    print(Solution.minSpeedOnTime(self=Solution, dist=[1, 3, 2], hour=2.7))
