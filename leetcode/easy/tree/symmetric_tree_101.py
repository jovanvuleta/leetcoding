# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(H) - height of the tree
        """
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)


if __name__ == "__main__":
    print(Solution.isSymmetric(self=Solution, root=TreeNode()))
