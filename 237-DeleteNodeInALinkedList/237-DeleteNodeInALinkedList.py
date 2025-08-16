# Last updated: 8/15/2025, 7:52:29 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp= node.val
        node.val = node.next.val
        node.next.val = temp
        node.next = node.next.next
        