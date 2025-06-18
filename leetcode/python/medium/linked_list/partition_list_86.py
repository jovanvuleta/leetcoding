# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after

        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next

        after_curr.next = None
        before_curr.next = after.next

        return before.next


if __name__ == "__main__":
    print(Solution.partition(head=[1, 4, 3, 2, 5, 2], x=3))
