class Solution:
    def countCollisions(self, directions: str) -> int:
        #stack problem
        stack = []

        collisions = 0

        for dir in directions:
            stack.append(dir)

            while len(stack) > 1:
                if (stack[-1] == 'L'):
                    if stack[-2] == 'S':
                        stack.pop()
                        collisions += 1
                    elif stack[-2] == 'R':
                        collisions += 2
                        stack.pop()
                        stack.pop()
                        stack.append('S')
                    else:
                        break
                else:
                    break

            while len(stack) > 1:
                if (stack[-1] == 'S') and (stack[-2] == 'R'):
                    stack.pop()
                    stack.pop()
                    stack.append('S')
                    collisions += 1
                else:
                    break
            
            while len(stack) > 1:
                if (stack[-1] == 'S' and stack[-2] == 'S'):
                    stack.pop()
                else:
                    break
            
        return collisions










