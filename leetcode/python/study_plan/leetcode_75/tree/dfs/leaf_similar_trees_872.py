# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(H) - height of the tree
        """
        def dfs(root):
            if not root:
                return ''
            if not root.left and not root.right:
                return str(root.val) + ','
            return dfs(root.left) + dfs(root.right)

        return dfs(root1) == dfs(root2)

    @staticmethod
    def leafSimilarSecond(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, arr):
            if not node:
                return

            if not node.left and not node.right:
                arr.append(node.val)
                return

            dfs(node.left, arr)
            dfs(node.right, arr)

        arr1, arr2 = [], []

        dfs(root1, arr1)
        dfs(root2, arr2)
        return arr1 == arr2


if __name__ == "__main__":
    root1 = TreeNode(4)
    left = TreeNode(2)
    right = TreeNode(6)
    left1 = TreeNode(1)
    right1 = TreeNode(3)

    root1.left = left
    root1.right = right
    left.left = left1
    left.right = right1

    root2 = TreeNode(4)
    left2 = TreeNode(2)
    right2 = TreeNode(6)
    left21 = TreeNode(1)
    right21 = TreeNode(3)

    root2.left = left2
    root2.right = right2
    left2.left = left21
    left2.right = right21
    print(Solution.leafSimilar(self=Solution, root1=root1, root2=root2))
