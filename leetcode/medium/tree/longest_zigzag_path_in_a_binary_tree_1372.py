from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N) - call stack
        """
        return max(self.helper(root.left, True, 0), self.helper(root.right, False, 0))

    def helper(self, root, isLeft, depth):
        if not root:
            return depth

        if isLeft:
            depth = max(
                depth,
                self.helper(root.right, False, depth + 1),
                self.helper(root.left, True, 0),
            )
        else:
            depth = max(
                depth,
                self.helper(root.right, True, depth + 1),
                self.helper(root.left, False, 0),
            )

        return depth


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
    print(Solution.longestZigZag(self=Solution, root=root))
