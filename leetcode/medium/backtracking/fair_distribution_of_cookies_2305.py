import heapq
from typing import List


class Solution:
    @staticmethod
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        """
            Time complexity: O(N * 2^k)
            Space complexity: O(k)
        """
        heap = [0] * k
        cookies.sort(reverse=True)

        for i in cookies:
            p = heapq.heappop(heap)
            p += i
            heapq.heappush(heap, p)

        cur_max = max(heap)

        def backtrack(people, c_id):
            nonlocal cur_max
            if c_id == len(cookies):
                cur_max = min(cur_max, max(people))
                return

            for c in range(c_id, len(cookies)):
                for p in range(len(people)):
                    if people[p] + cookies[c] < cur_max:
                        people[p] += cookies[c]
                        backtrack(people[:], c + 1)
                        people[p] -= cookies[c]
                return

        backtrack([0] * k, 0)
        return cur_max

    @staticmethod
    def distributeCookiesSecond(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        distribution = [0] * k

        def backtrack(i):
            nonlocal min_unfairness, distribution

            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(distribution))
                return

            # Bounding condition to stop a branch if unfairness already exceeds current optimal solution
            if min_unfairness <= max(distribution):
                return

            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]

        backtrack(0)
        return min_unfairness


if __name__ == "__main__":
    print(Solution.distributeCookies(self=Solution, cookies=[8, 15, 10, 20, 8], k=2))
