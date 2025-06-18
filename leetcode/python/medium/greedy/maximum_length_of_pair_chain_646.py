from typing import List


class Solution:
    @staticmethod
    def findLongestChain(pairs: List[List[int]]) -> int:
        """
            Intuition: Top-down memoization approach
            Time complexity: O(N * log(N))
            Space complexity: O(1)
        """
        pairs.sort(key=lambda x: x[1])
        cur, ans = float('-inf'), 0

        for pair in pairs:
            if cur < pair[0]:
                cur = pair[1]
                ans += 1

        return ans


if __name__ == "__main__":
    print(Solution.findLongestChain(pairs=[[1, 2], [2, 3], [3, 4]]))
