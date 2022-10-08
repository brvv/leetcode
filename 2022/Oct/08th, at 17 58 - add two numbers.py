# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getIntegerValue(self, l):
        total = 0
        for item in l:
            total = total * 10 + item
        return total
    
    def getLListVal(self, ll):
        value = []
        while ll:
            value += [ll.val]
            ll = ll.next
        return self.getIntegerValue(value[::-1])
    
    def addTwoNumbers(self, l1, l2):
        val1 = self.getLListVal(l1)
        val2 = self.getLListVal(l2)
        
        intRes = val1 + val2
        strRes = str(intRes)[::-1]
        
        startNode = ListNode()
        currentNode = startNode
        first = True
        

        for digit in strRes[:-1]:
            currentNode.val = int(digit)
            currentNode.next = ListNode()
            currentNode = currentNode.next

        currentNode.val = int(strRes[-1])
        return startNode