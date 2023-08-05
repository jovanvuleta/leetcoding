# Definition for a binary tree node.
from functools import lru_cache
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache
        def dfs(st, end):
            """
                Time Complexity: O(C(n))
                Space Complexity: O(n^2)
            """
            if st > end:
                return [None]
            ans = []
            for i in range(st, end + 1):
                left = dfs(st, i - 1)
                right = dfs(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i, l, r)
                        ans.append(root)
            return ans

        return dfs(1, n)


if __name__ == "__main__":
    print(Solution.generateTrees(self=Solution, n=3))
