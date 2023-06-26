# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        self.total = 0
        self.lookup = defaultdict(int)
        self.lookup[targetSum] = 1

        def dfs(node, root_sum):
            if not node:
                return
            root_sum += node.val
            self.total += self.lookup[root_sum]
            self.lookup[root_sum + targetSum] += 1
            dfs(node.left, root_sum)
            dfs(node.right, root_sum)
            self.lookup[root_sum + targetSum] -= 1

        dfs(root, 0)

        return self.total

    @staticmethod
    def pathSumSecond(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(1)
        """
        self.total = 0

        def helper(node, cur):
            if not node:
                return
            helper(node.left, cur + node.val)
            helper(node.right, cur + node.val)
            if cur + node.val == targetSum:
                self.total += 1

        def dfs(node):
            if not node:
                return
            helper(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.total


if __name__ == "__main__":
    root = TreeNode(3)
    left = TreeNode(1)
    right = TreeNode(4)
    left1 = TreeNode(3)
    right1 = TreeNode(5)
    right1left = TreeNode(1)

    root.left = left
    root.right = right
    left.left = left1
    right.right = right1
    right.left = right1left

    print(Solution.pathSum(self=Solution, root=root, targetSum=4))
