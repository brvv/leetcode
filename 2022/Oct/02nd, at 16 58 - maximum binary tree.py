# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxIndex(self, nums):
        maxvalue = nums[0]
        maxindex = 0
        
        for i, val in enumerate(nums):
            if val > maxvalue:
                maxvalue = val
                maxindex = i
        return maxindex
            
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def buildTree(nums):
            if (nums == []):
                return None
            
            else:
                root = TreeNode()

                maxIndex = self.getMaxIndex(nums)

                prefix = nums[:maxIndex] if maxIndex > 0 else []
                suffix = nums[maxIndex + 1:] if maxIndex + 1 < len(nums) else []

                maxval = nums[maxIndex]

                root.val = maxval
                root.left = buildTree(prefix)
                root.right = buildTree(suffix)
                
                return root
        
        root = buildTree(nums)
        return root