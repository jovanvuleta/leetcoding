# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [], []
        current = root

        while current or stack:
            while current:
                res.append(current.val)
                stack.append(current)
                current = current.left

            current = stack.pop()
            current = current.right
        return res
