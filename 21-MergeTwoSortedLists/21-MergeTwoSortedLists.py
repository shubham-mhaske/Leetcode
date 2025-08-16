# Last updated: 8/15/2025, 7:52:36 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) and (not list2):
            return list1
        if (not list1) and list2:
            return list2
        if (not list2) and list1:
            return list1
        
        head  =  None
        h1 = list1
        h2 = list2

        
        if h1.val <h2.val:
            head = h1
            h1 = h1.next
        else:
            head = h2
            h2 = h2.next
        temp = head
        while h1 and h2:
            if h1.val <h2.val:
                temp.next = h1
                temp = temp.next
                h1 = h1.next
            else:
                temp.next = h2
                temp = temp.next
                h2 = h2.next
        while h1:
            temp.next = h1
            temp = temp.next
            h1 = h1.next
        while h2:
            temp.next = h2
            temp = temp.next
            h2 = h2.next
        return head

                
        