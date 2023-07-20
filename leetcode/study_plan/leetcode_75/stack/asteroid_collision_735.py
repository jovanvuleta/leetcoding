from typing import List


class Solution:

    @staticmethod
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        stack = []

        for roid in asteroids:
            while stack and stack[-1] > 0 and roid < 0:
                if stack[-1] > -roid:
                    break
                elif stack[-1] == -roid:
                    stack.pop()
                    break
                elif stack[-1] < -roid:
                    stack.pop()
            else:
                stack.append(roid)
        return stack

    @staticmethod
    def asteroidCollisionThird(asteroids: List[int]) -> List[int]:
        stack = []

        for roid in asteroids:
            while stack and roid < 0 and stack[-1] > 0:
                if stack[-1] + roid < 0:
                    stack.pop()
                elif stack[-1] + roid > 0:
                    roid = 0
                else:
                    roid = 0
                    stack.pop()

            if roid:
                stack.append(roid)

        return stack

    @staticmethod
    def asteroidCollisionSecond(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for a in asteroids[1:]:
            while stack and stack[-1] > 0 > a and abs(a) > stack[-1]:
                stack.pop()

            if not stack:
                stack.append(a)
            elif stack[-1] > 0 and a < 0 and stack[-1] == abs(a):
                stack.pop()
            elif stack[-1] < 0 or a > 0 or abs(stack[-1]) < abs(a):
                stack.append(a)

        return stack


if __name__ == "__main__":
    print(Solution.asteroidCollision(self=Solution, asteroids=[10, 2, -5]))
