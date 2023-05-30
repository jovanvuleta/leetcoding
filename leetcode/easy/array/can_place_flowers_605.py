from typing import List


class Solution:
    @staticmethod
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        f = [0] + flowerbed + [0]

        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
                f[i] = 1
                n -= 1
        return n <= 0

    @staticmethod
    def canPlaceFlowersConstantSpaceSolution(self, flowerbed: List[int], n: int) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        empty = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)  # int division, round toward zero
                empty = 0
            else:
                empty += 1

        n -= empty // 2
        return n <= 0


if __name__ == "__main__":
    # print(Solution.canPlaceFlowers(self=Solution, flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2))
    print(Solution.canPlaceFlowersConstantSpaceSolution(self=Solution, flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2))
