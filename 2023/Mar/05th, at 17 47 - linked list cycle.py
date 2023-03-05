# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tort = head

        while hare and tort:
            hare = hare.next
            if hare:
                hare = hare.next
            else:
                return False
            tort = tort.next

            if tort == hare:
                return True
        
        return False