from typing import List


class Solution:
    """
        Intuition:
            The Intuition is to use backtracking approach to explore all possible combinations of taking or not
            taking transfer requests. It maintains a count of transfer requests and checks if the requests are balanced
            for each building. The maximum count of transfer requests that satisfies the balanced request condition is
            returned as the result.
        Time complexity: O(2^M * N)
        Space complexity: O(N+M)
        N is the number of buildings, and M is the number of requests.
    """
    def __init__(self):
        self.ans = 0

    def helper(self, start, requests, indegree, n, count):
        if start == len(requests):
            for i in range(n):
                if indegree[i] != 0:
                    return
            self.ans = max(self.ans, count)
            return

        # Take
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start + 1, requests, indegree, n, count + 1)

        # Not-take
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1
        self.helper(start + 1, requests, indegree, n, count)

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n
        self.helper(0, requests, indegree, n, 0)
        return self.ans
