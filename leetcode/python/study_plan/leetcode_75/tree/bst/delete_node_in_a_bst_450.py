# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
            Intuition: When we find the node to be deleted, we find the min from the right subtree of the node,
            (if there is right subtree) and we replace the node val with the min node val from the right subtree.
            Time complexity: O(N)
            Space complexity: O(N)
        """
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Find the min from right subtree
            curr = root.right
            while curr.left:
                curr = curr.left

            # Update the node that we are supposed to delete, with the min node value from the right subtree
            root.val = curr.val

            # Since now, we have 2 min node values, one on the node that was supposed to be deleted and one in the right
            # subtree, we are recursively calling the deletion of the min node value on the right subtree
            root.right = self.deleteNode(root.right, root.val)

        return root


if __name__ == "__main__":
    root = TreeNode(1)
    l = TreeNode(7)
    r = TreeNode(0)
    l1 = TreeNode(7)
    r1 = TreeNode(-8)
    root.left = l
    root.right = r
    l.left = l1
    l.right = r1
    print(Solution.deleteNode(self=Solution, root=root))
