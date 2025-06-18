# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
            Intuition: Build an undirected graph, and do BFS on it and keep count of the distance from the target node.
            Time complexity: O(N)
            Space complexity: O(N)
        """
        if not k:
            return [target.val]

        graph = collections.defaultdict(list)

        q = collections.deque([root])

        while q:
            node = q.popleft()

            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)

            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)

        res = []
        visited = set([target])
        q = collections.deque([(target, 0)])

        while q:
            node, distance = q.popleft()
            if distance == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        q.append((edge, distance + 1))

        return res

    @staticmethod
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.res = []
        self.found = False

        def dfs(node, depth):
            if not node:
                return

            if depth == k:
                self.res.append(node.val)

            if node.val == target.val:
                self.found = True

            dfs(node.left, depth + 1 if self.found else 0)
            dfs(node.right, depth + 1 if self.found else 0)

        dfs(root, 0)

        return self.res


if __name__ == "__main__":
    root = TreeNode(3)
    left = TreeNode(5)
    right = TreeNode(1)
    l_left1 = TreeNode(6)
    l_right1 = TreeNode(2)
    l_left2 = TreeNode(7)
    l_right2 = TreeNode(4)
    r_left1 = TreeNode(0)
    r_right1 = TreeNode(8)

    root.left = left
    root.right = right
    left.left = l_left1
    left.right = l_right1
    right.left = r_left1
    right.right = r_right1
    l_right1.left = l_left2
    l_right1.right = l_right2
    print(Solution.distanceK(self=Solution, root=root, target=left, k=2))
