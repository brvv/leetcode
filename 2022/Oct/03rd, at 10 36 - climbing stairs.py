class Solution(object):
    def climbStairs(self, n):
        ways = {}
        ways[1] = 1
        ways[0] = 1
        
        for stair_num in range(2, n+1):
            add_ways = 0
            if stair_num - 1 in ways:
                add_ways += ways[stair_num-1]
            if stair_num - 2 in ways:
                add_ways += ways[stair_num-2]
            ways[stair_num] = add_ways
        print(ways)
        return ways[n]
        