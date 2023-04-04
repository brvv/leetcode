class Solution:
    def isValidMutation(self, start, end):
        diff = 0
        for l1, l2 in zip(start, end):
            if l1 != l2:
                diff += 1
            
            if diff > 1:
                return False
        return diff == 1
    
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        cache = {}
        for mutation in bank:
            cache[mutation] = -1

        if endGene not in cache:
            return -1
        
        cache[startGene] = -1
        cache[endGene] = 0

        stack = []
        stack.append(endGene)
        currDepth = 0

        while True:
            newStack = []

            while len(stack) > 0:
                start = stack.pop()

                for mutation in cache:
                    if cache[mutation] == -1 and self.isValidMutation(start, mutation):
                        cache[mutation] = cache[start] + 1
                        newStack.append(mutation)
                
            stack = newStack
            if len(stack) == 0:
                break

        return cache[startGene]
        

