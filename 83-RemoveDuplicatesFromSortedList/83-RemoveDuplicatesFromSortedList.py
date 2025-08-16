# Last updated: 8/15/2025, 7:52:35 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        prev = head
        while curr.next:
            curr = prev.next
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
        return head