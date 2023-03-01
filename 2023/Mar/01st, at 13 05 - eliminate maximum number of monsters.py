class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        steps = []

        for mdist, mspeed in zip(dist, speed):
            minutes = math.ceil(mdist / mspeed)
            steps.append(minutes)

        
        heapq.heapify(steps)
        time_passed = 0
        killed = 0

        while len(steps) > 0:
            monster_time = heapq.heappop(steps) - time_passed

            if monster_time <= 0:
                return killed

            killed += 1
            time_passed += 1
        
        return killed

