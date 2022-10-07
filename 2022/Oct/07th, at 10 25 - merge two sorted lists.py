# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        startNode = None
        
        if list1.val <= list2.val:
            startNode = list1
        else:
            startNode = list2
            
        nextNode = None
        currentNode = startNode
            
        while list2 or list1:
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    nextNode = list1
                    list1 = list1.next
                else:
                    nextNode = list2
                    list2 = list2.next
                currentNode.next = nextNode
                currentNode = nextNode
            elif list1 is not None:
                nextNode = list1
                list1 = list1.next
                currentNode.next = nextNode
                currentNode = nextNode
            else:
                nextNode = list2
                list2 = list2.next
                currentNode.next = nextNode
                currentNode = nextNode
        return startNode