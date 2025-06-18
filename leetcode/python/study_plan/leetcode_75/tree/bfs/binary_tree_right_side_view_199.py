# Definition for a binary tree node.
from collections import deque, defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
            Intuition: BFS Solution
            Time Complexity: O(N)
            Space Complexity: O(N)
        """
        q, res = deque([root]), []

        while q:
            right_side = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)

            if right_side:
                res.append(right_side.val)

        return res

    @staticmethod
    def rightSideViewSecond(self, root: Optional[TreeNode]) -> List[int]:
        """
            Intuition: DFS Solution
            Time Complexity: O(N)
            Space Complexity: O(N)
        """
        l = defaultdict(int)

        def dfs(node, h):
            if not node:
                return

            if h not in l:
                l[h] = node.val

            # important to iterate first on the right side, since then the height will be populated
            # with the values from the right side, and when the call stack for left side comes, h will is already in l
            dfs(node.right, h + 1)
            dfs(node.left, h + 1)

        dfs(root, 0)
        return [val for val in l.values()]


if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    left_r = TreeNode(5)
    right_r = TreeNode(4)
    # right11 = TreeNode(5)
    # right1left = TreeNode(1)

    root.left = left
    root.right = right
    left.right = left_r
    right.right = right_r
    print(Solution.rightSideViewSecond(self=Solution, root=root))
