# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current:
            next_node = current.next
            
            if next_node.val == 0:
                if next_node.next is None:
                    current.next = None
                    return head
                else:
                    current = next_node
                    continue
            
            current.val += next_node.val
            current.next = next_node.next
        return head
            