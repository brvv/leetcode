class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        options = set({})
        cache = {}

        for num in nums:
            counts[num] += 1
            options.add(num)

        def delRec(index, arr):
            if index >= len(arr):
                return 0
            subproblem = index
            if subproblem in cache:
                return cache[subproblem]
            a1 = 0
            a2 = 0
            element = arr[index]
            #remove the element
            inc = 1 if index + 1 < len(arr) and arr[index + 1] - 1 != element else 2
            a1 = counts[element] * element + delRec(index + inc, arr)
                    
            #keep the element   
            a2 = delRec(index + 1, arr)
            cache[subproblem] = max(a1, a2)
            return cache[subproblem]
        
        return delRec(0, sorted(list(counts.keys())))