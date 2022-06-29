class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1
        pointerSum = numbers[pointer1] + numbers[pointer2]
        
        while (pointerSum != target):
            if pointerSum > target:
                pointer2 -= 1
            if pointerSum < target:
                pointer1 += 1
            pointerSum = numbers[pointer1] + numbers[pointer2]
        return [pointer1 + 1, pointer2 + 1]
            
        
        
        
'''
Pointer in the beginning and end
If sum too large, move the end pointer left
If sum too small, move the beg pointer right

'''