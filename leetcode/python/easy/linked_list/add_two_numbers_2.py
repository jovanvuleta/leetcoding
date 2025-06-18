from typing import Optional

from leetcode.easy.linked_list.helpers import build_linked_list, print_linked_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
        Time complexity: O(N)
        Space complexity: O(1)
    """

    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value + carry
            current.next = ListNode(total % 10)
            carry = total // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return head.next

    @staticmethod
    def addTwoNumbersSumString(l1: ListNode, l2: ListNode) -> ListNode:
        """
            Solution: Iterate over both lists separately and concatenate the int number to a string. Reverse them and then
            make a linked list from the sum of the reversed numbers.
            Time complexity: O(N + M) - n,m are the lengths of both given linked lists
            Space complexity: O(1) - 1 node created - head
        """
        d = n = ListNode(0)
        num1 = num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        res_str = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        for i in res_str:
            d.next = ListNode(int(i))
            d = d.next
        return n.next


if __name__ == "__main__":
    l1 = build_linked_list(l1=[3, 4, 2])
    l2 = build_linked_list(l1=[5, 6, 4])

    res = Solution.addTwoNumbersSumString(l1=l1, l2=l2)

    print_linked_list(node=res)
