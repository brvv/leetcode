class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        miss_right = -1
        
        for i in range(len(arr)-2, -1, -1):
            temp = arr[i]
            arr[i] = max(arr[i+1], miss_right)
            miss_right = temp
        arr[-1] = -1
        return arr