# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]

    @staticmethod
    def postorderTraversalSecondSolution(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)

        return res

    @staticmethod
    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(root: TreeNode):
            if root is None:
                return root

            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.right = node1
    node1.left = node2
    print(Solution.postorderTraversal(Solution, root))
