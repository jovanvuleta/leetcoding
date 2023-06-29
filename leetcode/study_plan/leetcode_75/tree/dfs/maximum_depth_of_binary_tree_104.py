# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(H) - height of the tree
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(self=Solution, root=root.left), self.maxDepth(self=Solution, root=root.right))

    @staticmethod
    def maxDepthIterativeBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level

    @staticmethod
    def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


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
    print(Solution.maxDepth(self=Solution, root=root))
