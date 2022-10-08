# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):    
    def addTwoNumbers(self, l1, l2):
        first = ListNode()
        current = first
        carry = 0

        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            
           
            
            val = (l1val + l2val + carry) % 10
            carry = (l1val + l2val + carry) // 10
            
            current.next = ListNode(val)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return first.next