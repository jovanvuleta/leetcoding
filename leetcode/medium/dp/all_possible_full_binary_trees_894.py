# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        """
            Intuition: Top-down(Memoization)
            Time complexity: O(N)
            Space complexity: O(N)
        """

        dp = {0: [], 1: [TreeNode()]}

        def backtrack(n):
            if n in dp:
                return dp[n]
            if n % 2 == 0:
                return []

            res = []

            for l in range(0, n):
                r = n - 1 - l
                left_trees, right_trees = backtrack(l), backtrack(r)

                for t1 in left_trees:
                    for t2 in right_trees:
                        res.append(TreeNode(0, t1, t2))
            dp[n] = res
            return res

        return backtrack(n)


if __name__ == "__main__":
    print(Solution.allPossibleFBT(self=Solution, n=7))
