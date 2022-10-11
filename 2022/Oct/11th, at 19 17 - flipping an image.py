class Solution:
    def flipRow(self, image, rowNum):
        left = 0
        right = len(image[rowNum]) - 1
        
        while left < right:
            image[rowNum][left], image[rowNum][right] = image[rowNum][right], image[rowNum][left]
            left += 1
            right -= 1
        return image

    def invertRow(self, image, rowNum):
        for i in range(len(image[rowNum])):
            image[rowNum][i] = 0 if image[rowNum][i] == 1 else 1
        return image
            
    
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i, row in enumerate(image):
            self.flipRow(image, i)
            self.invertRow(image, i)
            
        return image