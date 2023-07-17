# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            Intuition: Have 2 stacks for both input linked lists.
            Time complexity: O(N)
            Space complexity: O(N)
        """
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        res = None

        while stack1 or stack2 or carry:
            sum_ = carry

            if stack1:
                sum_ += stack1.pop()
            if stack2:
                sum_ += stack2.pop()

            node = ListNode(sum_ % 10)
            carry = sum_ // 10

            node.next = res
            res = node

        return res

    @staticmethod
    def addTwoNumbersSecond(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            Intuition: Reverse both input linked lists, perform addition with a carry, reverse the result linked list.
            Time complexity: O(N)
            Space complexity: O(N)
        """

        def reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node

            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        carry = 0
        dummy_head = ListNode(0)
        tail = dummy_head

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return reverse(dummy_head.next)

    @staticmethod
    def build_linked_list(l1: List[int]):
        head = ListNode(l1[0])
        curr = head

        for val in l1[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return head

    @staticmethod
    def print_linked_list(node: Optional[ListNode]):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")


if __name__ == "__main__":
    l1 = Solution.build_linked_list(l1=[7, 2, 4, 3])
    l2 = Solution.build_linked_list(l1=[5, 6, 4])
    print(Solution.addTwoNumbers(self=Solution, l1=l1, l2=l2).val)
