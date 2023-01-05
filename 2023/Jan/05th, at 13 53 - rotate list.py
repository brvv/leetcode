# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = deque()

        curr = head
        
        while curr:
            nodes.append(curr)
            curr = curr.next

        if len(nodes) <= 1:
            return head

        for i in range(k % len(nodes)):
            last_node = nodes.pop()
            second_last_node = nodes[-1]

            second_last_node.next = None
            last_node.next = nodes[0]
            nodes.appendleft(last_node)

        return nodes[0]