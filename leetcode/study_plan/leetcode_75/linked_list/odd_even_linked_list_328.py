# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        odd_h = o_curr = head
        even_h = e_curr = head.next

        while e_curr and e_curr.next:
            o_curr.next = e_curr.next
            o_curr = o_curr.next
            e_curr.next = o_curr.next
            e_curr = e_curr.next

        o_curr.next = even_h

        return odd_h


if __name__ == "__main__":
    # node7 = ListNode(6)
    # node6 = ListNode(2, node7)
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head_node = ListNode(1, node2)

    print(Solution.oddEvenList(self=Solution, head=head_node))
