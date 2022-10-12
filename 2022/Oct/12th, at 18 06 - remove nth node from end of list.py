# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None
        
        slow = head
        fast = head
        
        #total number of nodes
        fast_count = 1
        
        while fast:
            fast = fast.next
            if fast:
                fast_count += 1
            
        target_node = fast_count - n + 1
        
        slow_count = 1
        
        if target_node == 1:
            return head.next
        
        while slow_count + 1 < target_node:
            slow = slow.next
            if slow:
                slow_count += 1
            
        target = slow
        node_to_remove = slow.next

        if node_to_remove:
            target.next = node_to_remove.next
            
        return head