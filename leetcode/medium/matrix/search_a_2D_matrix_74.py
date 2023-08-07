from typing import List


class Solution:
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        """
            Time complexity: O(log(M) * log(N))
            Space complexity: O(1)
        """
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break

        if not l <= r:
            return False

        row = (l + r) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False


if __name__ == "__main__":
    print(Solution.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))
