# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def goodNodes(self, root: TreeNode) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(H) - height of the tree
        """

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)

    @staticmethod
    def goodNodesSecond(self, root: TreeNode) -> int:
        ans = 0
        q = deque()

        q.append((root, root.val))

        while q:
            node, maxval = q.popleft()
            if node.val >= maxval:
                ans += 1

            if node.left:
                q.append((node.left, max(maxval, node.val)))

            if node.right:
                q.append((node.right, max(maxval, node.val)))

        return ans


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
    print(Solution.goodNodes(self=Solution, root=root))
