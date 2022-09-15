class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_costs = [0 for item in cost]
        total_costs.append(0)
        
        for i in range(2, len(cost)+1):
            total_costs[i] = min(cost[i-1] + total_costs[i-1], cost[i-2] + total_costs[i-2])
        print(total_costs)
        return total_costs[-1]
        
        
        