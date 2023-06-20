# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        slow = fast = head
        stack = []
        mx = 0

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        while len(stack) > 0 and slow:
            mx = max(mx, stack.pop() + slow.val)
            slow = slow.next

        return mx

    @staticmethod
    def pairSumSecond(self, head: Optional[ListNode]) -> int:
        curr = head
        stack = []

        while curr:
            stack.append(curr.val)
            curr = curr.next

        n = len(stack)
        stack2 = []
        mx = 0

        while len(stack) > n / 2:
            stack2.append(stack.pop())

        while stack and stack2:
            mx = max(mx, stack.pop() + stack2.pop())

        return mx


if __name__ == "__main__":
    # node7 = ListNode(6)
    # node6 = ListNode(2, node7)
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head_node = ListNode(1, node2)

    print(Solution.pairSum(self=Solution, head=head_node))
