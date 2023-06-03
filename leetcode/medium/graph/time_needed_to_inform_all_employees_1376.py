from collections import deque, defaultdict
from typing import List


class Solution:
    @staticmethod
    def numOfMinutesBFS(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        graph = defaultdict(list)

        for idx, parent in enumerate(manager):
            graph[parent].append(idx)

        res = 0

        q = deque([(headID, informTime[headID])])

        while q:
            curr_emp, curr_time = q.popleft()
            res = max(res, curr_time)
            for report in graph[curr_emp]:
                q.append((report, curr_time + informTime[report]))

        return res

    @staticmethod
    def numOfMinutesDFS(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                subordinates[m].append(i)

        def dfs(node):
            if not subordinates[node]:
                return 0
            max_time = 0
            for sub in subordinates[node]:
                max_time = max(max_time, dfs(sub))
            return informTime[node] + max_time

        return dfs(headID)


if __name__ == "__main__":
    print(
        Solution.numOfMinutes(
            self=Solution,
            n=7,
            headID=6,
            manager=[1, 2, 3, 4, 5, 6, -1],
            informTime=[0, 6, 5, 4, 3, 2, 1]
        )
    )
