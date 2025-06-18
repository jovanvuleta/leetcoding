from typing import List


class Solution:

    @staticmethod
    def countNegatives(grid: List[List[int]]) -> int:
        """
            Time complexity: O(N + M)
            Space complexity: O(1)
        """
        # [
        #     [4,3,2,-1],
        #     [3,2,1,-1],
        #     [1,1,-1,-2],
        #     [-1,-1,-2,-3]
        # ]
        col = len(grid) - 1
        row = len(grid[0]) - 1
        i, j = 0, row
        count = 0

        while i <= col and j >= 0:
            if grid[i][j] < 0:
                count += len(grid) - i
                j -= 1
            else:
                i += 1

        return count

    @staticmethod
    def countNegativesBruteForce(grid: List[List[int]]) -> int:
        """
            Time complexity: O(N ^ 2)
            Space complexity: O(1)
        """
        col = len(grid) - 1
        row = len(grid[0]) - 1
        count = 0

        for i in range(col, -1, -1):
            for j in range(row, -1, -1):
                if grid[i][j] < 0:
                    count += 1

        return count


if __name__ == "__main__":
    result = Solution.countNegatives(
    )
