from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(l1: List[int]):
    head = ListNode(l1[0])
    curr = head

    for val in l1[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def print_linked_list(node: Optional[ListNode]):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
