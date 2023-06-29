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

    @staticmethod
    def equalPairsSecond(self, grid: List[List[int]]) -> int:
        rows = grid
        columns = list(zip(*grid))
        counter = 0
        for i in rows:
            for k in columns:
                if i == list(k):
                    counter += 1
        return counter

    @staticmethod
    def equalPairsThird(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0

        for i in range(n):
            for j in range(n):
                k = 0
                while k < n:
                    if grid[i][k] != grid[k][j]:
                        break
                    k += 1
                if k == n:  # R[i] == C[j]
                    ans += 1

        return ans


if __name__ == "__main__":
    print(Solution.equalPairs(self=Solution, grid=[
        [3, 2, 1],
        [1, 7, 6],
        [2, 7, 7]
    ]))
