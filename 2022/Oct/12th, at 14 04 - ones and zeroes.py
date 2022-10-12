class Solution:
    def __init__(self):
        self.max_size = 0
    
    def countBinaries(self, string):
        res = {}
        res[0] = 0
        res[1] = 0
        
        for s in string:
            res[int(s)] += 1
        return res
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strings = {}
        strings_counter = {}
        
        
        # ? ? ? prolly tuple(current, current_size)
        cache = set({})
        
        for string in strs:
            strings[string] =  self.countBinaries(string)
            strings_counter[string] = 1 + strings_counter.get(string, 0)
            
        # target = [0's 1's] current = [0's 1's]
        def dfs(target, current, current_size):
            self.max_size = max(self.max_size, current_size)
            if current[0] == target[0] and current[1] == target[1]:
                return 
            
            if tuple([current[0], current[1], current_size]) in cache:
                return
            
            
                
            for string in strings:
                if strings_counter[string] > 0:
                    count = strings[string]
                    if (current[0] + count[0] <= target[0] and current[1] + count[1] <= target[1]):
                        strings_counter[string] -= 1
                        dfs(target, [current[0] + count[0],current[1] + count[1]], current_size + 1)
                        strings_counter[string] += 1     
            
            cache.add(tuple([current[0], current[1], current_size]))
        dfs([m, n], [0, 0], 0)
        return self.max_size