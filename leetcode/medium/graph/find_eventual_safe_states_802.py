from typing import List


class Solution:
    @staticmethod
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
            Time complexity: O(E + V) - edges + vertices
            Space complexity: O(N)
        """
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
            safe[i] = True
            return safe[i]

        res = []
        for i in range(n):
            if dfs(i):
               res.append(i)

        return res


if __name__ == "__main__":
    print(Solution.eventualSafeNodes(self=Solution, graph=[[]]))
