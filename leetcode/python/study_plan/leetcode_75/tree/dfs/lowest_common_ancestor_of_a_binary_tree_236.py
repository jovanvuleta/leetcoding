# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            Time complexity: O(N)
            Space complexity: O(N) - call stack
        """
        if not root:
            return None

        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r


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
    print(Solution.lowestCommonAncestor(self=Solution, root=root))
