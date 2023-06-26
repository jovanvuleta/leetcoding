import heapq
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    @staticmethod
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        """
            Time complexity: O(N * log(K))
            Space complexity: O(K)
        """
        leftheap = costs[:candidates]
        rightheap = costs[max(candidates, len(costs) - candidates):]

        heapify(leftheap)
        heapify(rightheap)

        res = 0
        ln, rn = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            if not rightheap or (leftheap and leftheap[0] <= rightheap[0]):
                res += heappop(leftheap)
                if ln <= rn:
                    heappush(leftheap, costs[ln])
                    ln += 1
            else:
                res += heappop(rightheap)
                if ln <= rn:
                    heappush(rightheap, costs[rn])
                    rn -= 1
        return res

    @staticmethod
    def totalCostSecond(self, costs: List[int], k: int, candidates: int) -> int:
        """
            Time complexity: O(N * log(K))
            Space complexity: O(K)
        """
        h = []
        N = len(costs)
        left = candidates
        right = N - candidates

        for i in range(left):
            heapq.heappush(h, (costs[i], i, 1))

        for i in range(max(right, left), N):
            heapq.heappush(h, (costs[i], i, -1))

        right -= 1

        total = 0

        for _ in range(k):
            c, index, direction = heapq.heappop(h)
            total += c

            if left <= right:
                if direction == 1:
                    heapq.heappush(h, (costs[left], left, 1))
                    left += 1
                else:
                    heapq.heappush(h, (costs[right], right, -1))
                    right -= 1

        return total


if __name__ == "__main__":
    print(Solution.totalCost(self=Solution, costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4))
