# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # deque, extra memory
        def rotateRightDeque(head, k):
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

        # no extra memory, find rotation point
        def rotateRightSmart(head, k):
            if not head:
                return head

            list_len = 0

            list_start = head
            curr = head
            tail = None

            while curr:
                tail = curr
                curr = curr.next
                list_len += 1
            elements_to_rotate = k % list_len
            curr = head

            if elements_to_rotate == 0:
                return head

            for i in range(list_len - elements_to_rotate - 1):
                curr = curr.next

            newHead = curr.next
            curr.next = None
            tail.next = head
            return newHead
        return rotateRightSmart(head, k)

            
            
