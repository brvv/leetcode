# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        listAlen = 0
        listBlen = 0

        nodeA = headA

        while nodeA:
            listAlen += 1
            nodeA = nodeA.next

        nodeB = headB

        while nodeB:
            listBlen += 1
            nodeB = nodeB.next

        nodeA = headA
        nodeB = headB

        while listAlen > listBlen:
            nodeA = nodeA.next
            listAlen -= 1

        while listBlen > listAlen:
            nodeB = nodeB.next
            listBlen -= 1
        
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA

            nodeA = nodeA.next
            nodeB = nodeB.next
        return 
            