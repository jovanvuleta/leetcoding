from typing import List


class Solution:
    @staticmethod
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
            Intuition:
                Binary search + DFS
            Using binary search to find the day and until that day increment all the 1's up until the mid day
            (water the cells), and then use bfs to find if there is a path of 0's from top to bottom row.
            Time complexity: O(N * M * log(N)) - N, M(row, col), N is the binary search on the days
            Space complexity: O(N * M) - N, M(row, col)
        """
        left, right = 1, len(cells)
        res = -1

        while left <= right:
            mid = (left + right) // 2

            if self.is_possible(mid, row, col, cells):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res

    def is_possible(self, mid, n, m, cells) -> bool:
        grid = [[0] * m for _ in range(n)]

        # Mark all the water spots up until the mid day
        for i in range(mid):
            row, col = cells[i]
            grid[row - 1][col - 1] = 1

        visited = set()
        # Add all the top 0's indexes to the stack, if there is any
        stack = [(0, col) for col in range(m) if grid[0][col] == 0]

        while stack:
            row, col = stack.pop()

            # If there is 0 in the last row, that means there is a path and return True
            if row == n - 1:
                return True

            # Skip already visited spots
            if (row, col) in visited:
                continue

            visited.add((row, col))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dx, col + dy

                # Check if neighbours of the current cell has a zero (land), if yes then add it to the stack
                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 0:
                    stack.append((new_row, new_col))

        return False


if __name__ == "__main__":
    print(Solution.latestDayToCross(self=Solution, row=1, col=1, cells=[[1, 1], [2, 1], [1, 2], [2, 2]]))
