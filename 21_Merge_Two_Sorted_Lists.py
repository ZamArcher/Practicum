# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
# Return the head of the merged linked list.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    """Initialization of ListNode."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # list_1

        result = []
        while list1:
            result.append(list1.val)
            list1 = list1.next

        while list2:
            result.append(list2.val)
            list2 = list2.next

        result.sort()
        print(result)

        temp = ListNode(-1)
        head = temp
        for value in result:
            temp.next = ListNode(value)
            temp = temp.next
        head = head.next

        return head


both_lists = Solution()
list1 = [1, 2, 4]
list2 = [1, 3, 4]
# for el in list1:
#     list_1 = ListNode(el)
#     list_1 = list_1.next
# for el in list2:
#     list_2 = ListNode(el)
#     list_2 = list_2.next

temp = both_lists.mergeTwoLists(list1, list2)
while temp:
    print(temp.val)
    temp.next
