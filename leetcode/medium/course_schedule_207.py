from typing import List


class Solution:
    @staticmethod
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            Intuition: Topological sort
            Time complexity: O(C + P) - course + prerequisites
            Space complexity: O(N)
        """
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if preMap[course] == []:
                return True

            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


if __name__ == "__main__":
    print(Solution.canFinish(self=Solution, numCourses=5, prerequisites=[[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))
