# Last updated: 8/15/2025, 7:52:33 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast  == slow:
                fast = head
                while fast!= slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
            
        