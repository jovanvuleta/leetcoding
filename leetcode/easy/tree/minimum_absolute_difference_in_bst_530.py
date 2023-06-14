# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        curr = root
        prev = None
        res = float('inf')

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev:
                    res = min(res, curr.val - prev.val)
                prev = curr
                curr = curr.right
        return res

    @staticmethod
    def getMinimumDifferenceSecond(root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = []
        curr = root
        prev = None
        min_diff = float('inf')

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if prev:
                min_diff = min(min_diff, curr.val - prev.val)
            prev = curr
            curr = curr.right

        return min_diff


if __name__ == "__main__":
    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(6)
    left1 = TreeNode(1)
    right1 = TreeNode(3)

    root.left = left
    root.right = right
    left.left = left1
    left.right = right1

    print(Solution.getMinimumDifference(root=root))
