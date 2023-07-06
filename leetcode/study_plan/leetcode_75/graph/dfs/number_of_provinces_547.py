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

    @staticmethod
    def findCircleNumSecond(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        numConnected = 0

        # build graph:
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)

        # perform dfs:
        visited = set()

        def dfs(node: int) -> None:
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                numConnected += 1

        return numConnected


if __name__ == "__main__":
    print(Solution.findCircleNum(self=Solution, isConnected=[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
