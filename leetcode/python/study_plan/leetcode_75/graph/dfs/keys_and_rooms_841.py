from collections import deque
from typing import List


class Solution:
    @staticmethod
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
            Intuition: DFS
            Time complexity: O(N)
            Space complexity: O(N)
        """
        visited = set()

        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    dfs(i)

        dfs(0)

        return len(visited) == len(rooms)

    @staticmethod
    def canVisitAllRoomsBFS(self, rooms):
        """
            Intuition: BFS
        """
        N = len(rooms)
        visited = set()
        q = deque([0])

        while q:
            curr_room = q.popleft()
            visited.add(curr_room)
            for key in rooms[curr_room]:
                if key not in visited:
                    q.append(key)
        return len(visited) == N


if __name__ == "__main__":
    print(Solution.canVisitAllRooms(self=Solution, rooms=[[1, 3], [3, 0, 1], [2], [0]]))
