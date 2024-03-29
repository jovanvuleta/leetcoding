from collections import deque
from typing import List


class Solution:
    @staticmethod
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
            Intuition: BFS - to find the shortest path to exit.
            Time complexity: O(N)
            Space complexity: O(1)
        """
        rows, cols = len(maze), len(maze[0])
        start = tuple(entrance)
        q = deque([start])
        res = 0
        visit = set([start])

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                # Base case - checks if the user reached the border exit
                if [r, c] != entrance and (r == 0 or c == 0 or r == rows - 1 or c == cols - 1):
                    return res

                # Move the user in 4 possible directions
                for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    row, col = r + dr, c + dc
                    # Check if within the grid and add only empty cells
                    if 0 <= row < rows and 0 <= col < cols and maze[row][col] == "." and (row, col) not in visit:
                        q.append((row, col))
                        visit.add((row, col))

            res += 1

        return -1


if __name__ == "__main__":
    print(Solution.nearestExit(
        self=Solution,
        maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
        entrance=[1, 2])
    )
