# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while True:
                if len(stack) == 0 or stack[-1] < 0 or a > 0:
                    stack.append(a)
                    break
                else:
                    if (stack[-1]) > -a:
                        break
                    elif stack[-1] == -a:
                        stack.pop()
                        break
                    else:
                        stack.pop()
        return stack