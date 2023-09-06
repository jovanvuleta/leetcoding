# Definition for singly-linked list.
from typing import Optional, List

from leetcode.easy.linked_list.helpers import build_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        output = []
        cur, n = head, 0

        while cur:
            n += 1
            cur = cur.next

        part, left = n // k, n % k
        cur = head
        prev = None

        for _ in range(k):
            output.append(cur)
            for _ in range(part):
                if cur:
                    prev = cur
                    cur = cur.next
            if left and cur:
                prev = cur
                cur = cur.next
                left -= 1
            if prev:
                prev.next = None

        return output


if __name__ == "__main__":
    l1 = build_linked_list(l1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(Solution.splitListToParts(head=l1, k=3))
