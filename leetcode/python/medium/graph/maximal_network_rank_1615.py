import collections
import itertools
from typing import List


class Solution:
    @staticmethod
    def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(N^2)
        """
        graph = collections.defaultdict(set)

        for city1, city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)

        res = 0

        for city1, city2 in itertools.combinations(graph.keys(), 2):
            print(str(city1) + " -> " + str(city2))
            has_connection = 1 if city1 in graph[city2] else 0

            city1_connections = len(graph[city1])
            city2_connections = len(graph[city2])

            res = max(res, city1_connections + city2_connections - has_connection)

        # Without itertools, way to get combinations
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if j in graph[i]:
        #             res = max(res, len(graph[i]) + len(graph[j]) - 1)
        #         else:
        #             res = max(res, len(graph[i]) + len(graph[j]))

        return res


if __name__ == "__main__":
    print(Solution.maximalNetworkRank(roads=[[0, 1], [0, 3], [1, 2], [1, 3]]))
