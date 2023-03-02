# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        if head is None:
            return head

        while head:
            nodes.append(head)
            head = head.next
        
        s_nodes = sorted(nodes, key= lambda a : a.val)
        
        nhead = s_nodes[0]
        node = nhead

        for item in s_nodes[1:]:
            node.next = item
            node = item
        
        node.next = None
    
        return nhead
