class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        nums = set({})

        for i in range(0, len(s) - k + 1):
            frame = s[i : i + k]
            frame_val = int(frame, 2)
            nums.add(frame_val)
        
        for i in range(0, (2 ** k) ):
            if i not in nums:
                return False
        return True