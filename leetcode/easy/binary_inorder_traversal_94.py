from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        stack, res = [], []

        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            res.append(current.val)
            current = current.right
        return res

    @staticmethod
    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root: TreeNode):
            if root is None:
                return root

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.right = node1
    node1.left = node2
    print(Solution.inorderTraversal(self=Solution, root=root))
