from typing import List


class Solution:
    @staticmethod
    def maxArea(self, height: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res


if __name__ == "__main__":
    print(Solution.maxArea(self=Solution, height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
