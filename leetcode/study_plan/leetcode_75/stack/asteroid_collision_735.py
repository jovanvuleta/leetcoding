from typing import List


class Solution:

    @staticmethod
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        res = []
        for asteroid in asteroids:
            while res and res[-1] > 0 and asteroid < 0:
                if res[-1] > -asteroid:
                    break
                elif res[-1] == -asteroid:
                    res.pop()
                    break
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
            else:
                res.append(asteroid)
        return res

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
