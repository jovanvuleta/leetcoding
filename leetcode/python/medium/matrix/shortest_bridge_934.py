from collections import deque
from typing import List


class Solution:
    @staticmethod
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
            Topics: BFS, DFS, Matrix
            Solution: Using first DFS to mark the island 1's as visited, and after that doing BFS to find the path to
            the next island.
            Time complexity: O(N^2)
            Space complexity: O(N^2) - because of population of both queue(BFS) and visit set(DFS)
        """

        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N

        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        if invalid(curR, curC) or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append([curR, curC])
                        visit.add((curR, curC))
                res += 1

        N = len(grid)
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()


if __name__ == "__main__":
    print(Solution.shortestBridge(self=Solution, grid=[[0, 1], [1, 0]]))
