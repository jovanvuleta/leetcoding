from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            Solution: Iterate over both lists and compare the values. For the lower value, move the pointer and
            continue the comparison. If one of the list is larger than another, when you get to the end of one,
            append the second one to the tail and return.
            Time complexity: O(N)
            Space complexity: O(N)
        """
        curr1 = list1
        curr2 = list2

        head_res = ListNode()
        res = head_res

        while curr1 is not None and curr2 is not None:
            if curr1.val == curr2.val:
                res.next = curr1
                curr1 = curr1.next
            elif curr1.val < curr2.val:
                res.next = curr1
                curr1 = curr1.next
            else:
                res.next = curr2
                curr2 = curr2.next

            res = res.next

        if curr1 is None:
            res.next = curr2
        else:
            res.next = curr1

        return head_res.next

    @staticmethod
    def createListNodesFromList(node_val_list: [ListNode]) -> ListNode:
        head = ListNode()
        curr = head
        for num in node_val_list:
            curr.next = ListNode(val=num)
            curr = curr.next

        return head.next


if __name__ == "__main__":
    list1 = Solution.createListNodesFromList(node_val_list=[1, 2, 4])
    list2 = Solution.createListNodesFromList(node_val_list=[1, 3, 4])
    print(Solution.mergeTwoLists(self=Solution, list1=list1, list2=list2))
