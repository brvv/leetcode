class Solution:
    
    def doMath(self, val1, val2, operand):
        if operand == "+":
            return val2 + val1
        elif operand == "-":
            return val2 - val1
        elif operand == "*":
            return val2 * val1
        else:
            return val2/val1
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operands = ['+', '-', '*', '/']
        
        for item in tokens:
            if item in operands:
                val1 = stack.pop()
                val2 = stack.pop()
                res = self.doMath(int(val1), int(val2), item)
                stack.append(str(int(res)))
            else:
                stack.append(item)
        return stack[0]