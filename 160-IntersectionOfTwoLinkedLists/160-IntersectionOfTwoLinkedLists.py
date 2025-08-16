# Last updated: 8/15/2025, 7:52:32 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        tempA = headA
        tempB = headB
        lenA = 0
        lenB = 0

        while tempA:
            lenA+=1
            tempA = tempA.next
        while tempB:
            lenB+=1
            tempB= tempB.next
        tempA = headA
        tempB = headB
        if lenA>lenB:
            for _ in range(lenA-lenB):
                tempA = tempA.next
        else:
            for _ in range(lenB-lenA):
                tempB = tempB.next
        while tempA and tempB:
            if tempA == tempB:
                return tempA
            tempA=tempA.next
            tempB = tempB.next
        return None

        

        