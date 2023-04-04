class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        heap = []
        s = sum(reward2)

        
        for i in range(len(reward2)):
            r1 = reward1[i]
            r2 = reward2[i]
            
            heappush(heap, [-(r1 - r2), i])
        
        
        for _ in range(k):
            item = heappop(heap)
            index = item[1]
            r1 = reward1[index]
            r2 = reward2[index]
            
            s -= r2
            s += r1
        return s
        