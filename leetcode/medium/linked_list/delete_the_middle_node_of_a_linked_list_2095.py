# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        slow = fast = node = head
        if fast.next is None:
            return None
        while fast and fast.next:
            node = slow
            slow = slow.next
            fast = fast.next.next

        node.next = slow.next
        return head

    @staticmethod
    def deleteMiddleSecond(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        curr = head

        while curr is not None:
            size += 1
            curr = curr.next

        if size == 1:
            return None

        mid = size // 2

        curr = head

        for i in range(mid):
            if i == mid - 1:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


if __name__ == "__main__":
    node7 = ListNode(6)
    node6 = ListNode(2, node7)
    node5 = ListNode(1, node6)
    node4 = ListNode(7, node5)
    node3 = ListNode(4, node4)
    node2 = ListNode(3, node3)
    head_node = ListNode(1, node2)

    print(Solution.deleteMiddle(self=Solution, head=head_node))
