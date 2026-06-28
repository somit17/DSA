class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] 
        for asteroid in asteroids:
            #Condition to collision happen
            while len(stack) > 0 and asteroid < 0 and stack[-1] > 0:
                total = asteroid + stack[-1]
                if total < 0:
                    stack.pop()
                elif total > 0:
                    asteroid = 0
                else:
                    stack.pop()
                    asteroid = 0

            if asteroid!=0:
                stack.append(asteroid)

        return stack

        