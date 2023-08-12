from typing import List


class Solution:
    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        """
            Intuition: DP
            Time complexity: O(N * M)
            Space complexity: O(N)
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N - 1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]

        return dp[0]

    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        """
            Intuition: Brute Force
            Time complexity: O(N * M)
            Space complexity: O(N * M)
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(M - 1, N - 1): 1}

        def dfs(r, c):
            if (r, c) == (2, 2):
                print("here")
            if r == M or c == N or obstacleGrid[r][c]:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[(r, c)]

        return dfs(0, 0)


if __name__ == "__main__":
    print(Solution.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
