import collections
import heapq
from typing import List


class Solution:
    @staticmethod
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
            Time complexity: O(E * log(V))
            Space complexity: O(V)
        """
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        pq = [(-1, start)]
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end:
                return prob * -1
            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * edgeProb, nei))

        return 0


if __name__ == "__main__":
    print(Solution.maxProbability(
        self=Solution, n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2)
    )
