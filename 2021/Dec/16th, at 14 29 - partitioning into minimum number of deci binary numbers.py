class Solution:
    def minPartitions(self, n: str) -> int:
        highest = int(n[0])
        for digit in n[1:]:
            if int(digit) > highest:
                highest = int(digit)
        return highest