class Solution:
    def hammingWeight(self, n: int) -> int:
        sumBits = 0
        currentN = n
        currentBitNumber = 32

        while (currentN != 0 and currentBitNumber >= 0):
            currentSum = 2 ** currentBitNumber
            if currentN >= currentSum:
                currentN -= currentSum
                sumBits += 1
            else:
                currentBitNumber -= 1
        return sumBits