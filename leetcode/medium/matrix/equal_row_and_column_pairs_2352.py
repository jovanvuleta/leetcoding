import collections
from typing import List


class Solution:
    @staticmethod
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        counter = collections.Counter()

        for row in grid:
            counter[tuple(row)] += 1

        total = 0
        N = len(grid)
        for i in range(N):
            now = []
            for j in range(N):
                now.append(grid[j][i])
            total += counter[tuple(now)]
        return total


if __name__ == "__main__":
    print(Solution.equalPairs(self=Solution, grid=[
        [3, 2, 1],
        [1, 7, 6],
        [2, 7, 7]
    ]))
