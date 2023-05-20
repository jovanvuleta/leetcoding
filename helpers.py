from leetcode.easy.add_two_numbers_2 import ListNode


def createListNodesFromList(node_val_list: [ListNode]) -> ListNode:
    head = ListNode()
    curr = head
    for num in node_val_list:
        curr.next = ListNode(val=num)
        curr = curr.next

    return head.next
