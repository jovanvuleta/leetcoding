from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(N)
        """

        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        visited = set()
        res = 0

        for start in range(len(isConnected)):
            if start not in visited:
                res += 1
            dfs(start)

        return res


if __name__ == "__main__":
    print(Solution.findCircleNum(self=Solution, isConnected=[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
