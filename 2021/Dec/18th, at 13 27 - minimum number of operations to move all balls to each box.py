class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        parsed_boxes = [int(char) for char in boxes]
        if len(parsed_boxes) < 2:
            return [0] * len(parsed_boxes)

        leftArray = self.calculateLeftArray(parsed_boxes)
        rightArray = self.calculateRightArray(parsed_boxes)
        return [left + right for left, right in zip(leftArray, rightArray)]

    def calculateLeftArray(self, boxes: List[int]) -> List[int]:
        answer = [[0, 0] for _ in range(len(boxes))]
        answer[-1] = [0, boxes[-1]]

        for i in range(len(boxes)-2, -1, -1):
            new_val = boxes[i] + answer[i+1][1]
            new_moves = answer[i+1][0] + answer[i+1][1]
            answer[i] = [new_moves, new_val]

        return [pair[0] for pair in answer]

    def calculateRightArray(self, boxes: List[int]) -> List[int]:
        answer = [[0, 0] for _ in range(len(boxes))]
        answer[0] = [0, boxes[0]]

        for i in range(1, len(boxes)):
            new_val = boxes[i] + answer[i-1][1]
            new_moves = answer[i-1][0] + answer[i-1][1]
            answer[i] = [new_moves, new_val]

        return [pair[0] for pair in answer]
    
