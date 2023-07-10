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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.min_depth = float('inf')

        def dfs(node, depth):
            if not node:
                return

            if not node.left and not node.right:
                self.min_depth = min(self.min_depth, depth + 1)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return self.min_depth

    @staticmethod
    def minDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        min_depth = float('inf')
        depth = 1

        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return min_depth

    @staticmethod
    def minDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        min_depth = float('inf')
        level = 1

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    min_depth = min(min_depth, level)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level += 1

        return min_depth


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
    print(Solution.minDepth(self=Solution, root=root))
