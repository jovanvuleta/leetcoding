from typing import List


class Solution:
    @staticmethod
    def PredictTheWinner(nums: List[int]) -> bool:
        """
            Intuition: Minmax gametheory problem solved by dp using memoization.
            Time complexity: O(N^2)
            Space complexity: O(N^2)
        """
        N = len(nums)
        has_cache = [[False] * (N + 1) for _ in range(N + 1)]
        cache = [[None] * (N + 1) for _ in range(N + 1)]

        def score(left, right):
            if left > right:
                return 0

            if has_cache[left][right]:
                return cache[left][right]

            score_left = nums[left] - score(left + 1, right)
            score_right = nums[right] - score(left, right - 1)
            has_cache[left][right] = True
            cache[left][right] = max(score_left, score_right)

            return cache[left][right]

        return score(0, N - 1) >= 0


if __name__ == "__main__":
    print(Solution.PredictTheWinner(nums=[1, 5, 233, 7]))
