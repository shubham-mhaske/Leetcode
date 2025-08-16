# Last updated: 8/15/2025, 7:52:37 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        h1 = l1
        h2 = l2
        head = ListNode(val=0,next=None)
        result = head
        while h1 and h2:
            sum = h1.val + h2.val + carry
            result.next = ListNode(sum%10)
            carry = sum//10
            result = result.next
            h1 = h1.next
            h2=h2.next
        
        while h1:
            sum = h1.val + carry
            result.next = ListNode(sum%10)
            carry = sum//10
            result = result.next
            h1 = h1.next

        while h2:
            sum = h2.val + carry
            result.next = ListNode(sum%10)
            carry = sum//10
            result = result.next
            h2 = h2.next
        if carry!= 0:
            result.next = ListNode(carry)
        
        return head.next

        