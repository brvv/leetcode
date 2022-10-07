class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        
        for i, letter in enumerate(s):
            if letter not in hashmap:
                hashmap[letter] = [i, i]
            else:
                hashmap[letter] = [hashmap[letter][0], i]
                
        res = []
        
        for letter in hashmap:
            interval = hashmap[letter]
            
            if len(res) > 0:
                last_interval = res[-1]
                if interval[0] >= last_interval[1]:
                    res.append(interval)
                elif last_interval[0] <= interval[0] <= interval[1] <= last_interval[1]:
                    pass
                elif last_interval[0] <= interval[0] and interval[1] >= last_interval[1]:
                    res[-1][1] = interval[1]
                else:
                    print("Why here?", interval, last_interval)
                    
            else:
                res.append(interval)
        print(res)
        return [i-x+1 for [x, i] in res]