# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val < list2.val:
            new_list_head = list1
            list1 = list1.next
        else:
            new_list_head = list2
            list2 = list2.next
            
        current_pointer = new_list_head
        
        
        while True:
            if list1 == None and list2 == None:
                break            
            elif list2 == None or (list1 and list1.val < list2.val):
                current_pointer.next = list1
                list1 = list1.next
            elif list1 == None or (list2 and list2.val <= list1.val):
                current_pointer.next = list2
                list2 = list2.next
            current_pointer = current_pointer.next
        return new_list_head
    
