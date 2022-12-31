class DoubleEndedPointer:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.rear = None
        self.front = None
        self.max_size = k
        self.elements = 0

    def _canAdd(self):
        return self.elements < self.max_size

    def _canRemove(self):
        return self.elements > 0

    def insertFront(self, value: int) -> bool:
        node = DoubleEndedPointer(value)
        
        if self._canAdd():
            if self.elements == 0:
                self.rear = node
                self.front = node
            else:
                self.front.right = node
                self.front.right.left = self.front
                self.front = self.front.right
            self.elements += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        node = DoubleEndedPointer(value)
        
        if self._canAdd():
            if self.elements == 0:
                self.rear = node
                self.front = node
            else:
                self.rear.left = node
                self.rear.left.right = self.rear
                self.rear = self.rear.left
            self.elements += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self._canRemove():
            if self.elements == 1:
                self.rear = None
                self.front = None
            else:
                self.front = self.front.left
                self.front.right = None
            self.elements -= 1
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self._canRemove():
            if self.elements == 1:
                self.rear = None
                self.front = None
            else:
                self.rear = self.rear.right
                self.rear.left = None
            self.elements -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.value
        

    def isEmpty(self) -> bool:
        return self.elements == 0
        

    def isFull(self) -> bool:
        return not self._canAdd()
        
'''
["MyCircularDeque","insertFront","getRear","deleteLast","getRear","insertFront","insertFront","insertFront","insertFront","isFull","insertFront","isFull","getRear","deleteLast","getFront","getFront","insertLast","deleteFront","getFront","insertLast","getRear","insertLast","getRear","getFront","getFront","getFront","getRear","getRear","insertFront","getFront","getFront","getFront","getFront","deleteFront","insertFront","getFront","deleteLast","insertLast","insertLast","getRear","getRear","getRear","isEmpty","insertFront","deleteLast","getFront","deleteLast","getRear","getFront","isFull","isFull","deleteFront","getFront","deleteLast","getRear","insertFront","getFront","insertFront","insertFront","getRear","isFull","getFront","getFront","insertFront","insertLast","getRear","getRear","deleteLast","insertFront","getRear","insertLast","getFront","getFront","getFront","getRear","insertFront","isEmpty","getFront","getFront","insertFront","deleteFront","insertFront","deleteLast","getFront","getRear","getFront","insertFront","getFront","deleteFront","insertFront","isEmpty","getRear","getFront","getRear","getRear","deleteFront","getRear","isEmpty","deleteFront","insertFront","insertLast","deleteLast"]
[null,true,89,true,-1,true,true,true,true,false,true,false,19,true,45,45,true,true,82,true,98,true,99,82,82,82,99,99,true,8,8,8,8,true,true,75,true,true,true,59,59,59,false,true,true,22,true,98,22,false,false,true,75,true,74,true,21,true,true,74,false,63,63,true,true,76,76,true,true,74,true,26,26,26,67,true,false,36,36,true,true,true,true,87,74,87,true,85,true,true,false,74,74,74,74,true,74,false,true,true,true,true]
[null,true,89,true,-1,true,true,true,true,false,true,false,19,true,45,45,true,true,82,true,98,true,99,82,82,82,99,99,true,8,8,8,8,true,true,75,true,true,true,59,59,59,false,true,true,22,true,59,22,false,false,true,75,true,35,true,21,true,true,35,false,63,63,true,true,76,76,true,true,35,true,26,26,26,67,true,false,36,36,true,true,true,true,87,35,87,true,85,true,true,false,35,35,35,35,true,35,false,true,true,true,true]
'''

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()