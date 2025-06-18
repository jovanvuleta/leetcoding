from typing import List


class Solution:
    @staticmethod
    def deleteGreatestValue(grid: List[List[int]]) -> int:
        """
            Time complexity: O(N log(N))
            Space complexity: O(N)
        """
        res = 0

        for row in grid:
            row.sort()

        R = len(grid)
        C = len(grid[0])

        for i in range(C):
            mx = grid[0][i]
            for j in range(R):
                mx = max(mx, grid[j][i])
            res += mx

        return res

    @staticmethod
    def deleteGreatestValueSecond(grid: List[List[int]]) -> int:
        res = 0

        for j in range(len(grid[0])):
            curr_max = 0
            for i in range(len(grid)):
                row_max = max(grid[i])
                curr_max = max(curr_max, row_max)
                max_index = grid[i].index(row_max)
                grid[i][max_index] = 0

            res += curr_max

        return res


if __name__ == "__main__":
    print(Solution.deleteGreatestValue(grid=[[1, 2, 4], [3, 3, 1]]))
