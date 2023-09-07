# Definition for singly-linked list.
from typing import Optional

from leetcode.easy.linked_list.helpers import build_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        dummy = ListNode(0, head)

        left_prev, cur = dummy, head

        for i in range(left - 1):
            left_prev, cur = cur, cur.next

        prev = None
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        left_prev.next.next = cur
        left_prev.next = prev

        return dummy.next


if __name__ == "__main__":
    l1 = build_linked_list(l1=[1, 2, 3, 4, 5])
    print(Solution.reverseBetween(head=l1, left=2, right=4))
