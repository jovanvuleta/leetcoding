from typing import Optional

from leetcode.easy.linked_list.helpers import build_linked_list


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    @staticmethod
    def copyRandomList(head: Optional[Node]) -> Optional[Node]:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        oldToCopy = {None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]


if __name__ == "__main__":
    l1 = build_linked_list(l1=[1, 2, 4, 3])
    print(Solution.copyRandomList(head=l1))
