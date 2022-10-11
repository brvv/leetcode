class Solution:
    def isValidBracket(self, s):
        stack = []
        
        for letter in s:
            if letter == "(":
                stack.append(letter)
            elif letter == ")":
                if len(stack)>0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(letter)
        return not len(stack) > 0
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        stack = []
        
        for letter in s:
            if letter == "(":
                stack.append(letter)
            elif letter == ")":
                if len(stack)>0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(letter)
                    
        
        
        if len(stack) == 0:
            return [s]
        
        invalid_count = {}
        
        for par in stack:
            invalid_count[par] = 1 + invalid_count.get(par, 0)
            
        res = set({})
        cache = set({})
        
        
        def dfs(original, level=0, valid="", openb=0, closedb=0):
            if level >= len(original):
                if self.isValidBracket(valid):
                    res.add(valid)
                cache.add(tuple([valid, level]))
                return
        
            if tuple([valid, level]) in cache:
                return
            
            
            current_symbol = original[level]
            
            openb += 1 if current_symbol == "(" else 0
            closedb  += 1 if current_symbol == ")" else 0
            
            if current_symbol not in ['(', ')']:
                #if symbol, keep going
                dfs(original, level + 1, valid + current_symbol)
            else:
                #if bracket,
                
                #include the current bracket
                dfs(original, level + 1, valid + current_symbol)
                
                #do no include the current bracket
                if (current_symbol in invalid_count and invalid_count[current_symbol] > 0):
                    invalid_count[current_symbol] -= 1
                    dfs(original, level + 1, valid)
                    invalid_count[current_symbol] += 1
            cache.add(tuple([valid, level]))
        dfs(s)
        return res