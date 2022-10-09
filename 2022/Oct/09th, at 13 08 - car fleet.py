class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, s, (target - pos)/s] for s, pos in zip(speed, position)]
        sorted_cars = sorted(cars, key=lambda x:x[0], reverse=True)
        
        stack = []
        
        for [pos, s, time] in sorted_cars:
            stack.append([pos, s, time])
            while len(stack) > 1 and stack[-2][2] >= stack[-1][2]:
                stack.pop()
            
        return len(stack)