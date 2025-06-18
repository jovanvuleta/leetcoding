import math
from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def maximumDetonation(bombs: List[List[int]]) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(N)
        """
        def dfs(node):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child)

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j:
                    continue

                if bombs[i][2] >= math.sqrt((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2):
                    graph[i].append(j)

        res = 0

        for i in range(len(bombs)):
            visited = set([i])
            dfs(i)
            res = max(res, len(visited))

        return res


if __name__ == "__main__":
    print(Solution.maximumDetonation(bombs=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]))
