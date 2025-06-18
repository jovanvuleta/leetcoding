# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        curr, prev = head, None

        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr

        return prev

    @staticmethod
    def printLinkedList(head: Optional[ListNode]):
        while head:
            print(str(head.val) + " -> ")
            head = head.next


if __name__ == "__main__":
    n4 = ListNode(5)
    n3 = ListNode(4, n4)
    n2 = ListNode(3, n3)
    n1 = ListNode(2, n2)
    head = ListNode(1, n1)
    Solution.printLinkedList(Solution.reverseList(self=Solution, head=head))
