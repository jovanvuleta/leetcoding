# Definition for a binary tree node.
import sys
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        level = 1
        q = deque([root])
        dic = {}

        while q:
            a = []
            for i in range(len(q)):
                node = q.popleft()
                a.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            dic[level] = sum(a)
            level += 1

        return max(dic, key=dic.get)

    @staticmethod
    def maxLevelSumSecond(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res, level = 0, 1
        q = deque([root])
        mx = -sys.maxsize

        while q:
            q_val = [node.val for node in q]
            if sum(q_val) > mx:
                mx = sum(q_val)
                res = level
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return res


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
    print(Solution.maxLevelSum(self=Solution, root=root))
