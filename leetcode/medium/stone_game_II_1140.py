from typing import List


class Solution:
    @staticmethod
    def stoneGameII(self, piles: List[int]) -> int:
        """
            Time complexity: O(N^3)
            Space complexity: O(N^2)
        """
        dp = {}

        # Num of stones Alice gets
        def dfs(alice, i, M):
            if i == len(piles):
                return 0
            if (alice, i, M) in dp:
                return dp[(alice, i, M)]

            res = 0 if alice else float("inf")
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                total += piles[i + X - 1]
                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))
            dp[(alice, i, M)] = res
            return res

        return dfs(True, 0, 1)


if __name__ == "__main__":
    print(Solution.stoneGameII(self=Solution, piles=[2,7,9,4,4]))
