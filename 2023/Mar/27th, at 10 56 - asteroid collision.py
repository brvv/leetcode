class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while len(stack) > 0:
                    if stack[-1] > abs(asteroid):
                        break
                    elif stack[-1] < 0 and asteroid < 0:
                        stack.append(asteroid)
                        break
                    elif stack[-1] < abs(asteroid):
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(asteroid)
        return stack
