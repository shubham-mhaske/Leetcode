# Last updated: 8/15/2025, 7:52:31 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next= curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
            
        