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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
            Time complexity: O(log(N))
            Space complexity: O(H) - H - height of the tree
        """
        def dfs(root):
            if not root:
                return None

            if root.val == val:
                return root

            if val > root.val:
                return dfs(root.right)
            else:
                return dfs(root.left)

        return dfs(root)

    @staticmethod
    def searchBST_BFS(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.val == val:
                    return node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return None

    @staticmethod
    def searchBST_DFS(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return None


if __name__ == "__main__":
    root = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(7)
    left1 = TreeNode(1)
    right1 = TreeNode(3)

    root.left = left
    root.right = right
    left.left = left1
    left.right = right1

    print(Solution.searchBST_BFS(self=Solution, root=root, val=2))
