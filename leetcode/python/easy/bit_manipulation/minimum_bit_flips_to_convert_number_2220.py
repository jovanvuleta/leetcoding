class Solution:
    @staticmethod
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        count = 0
        while xor != 0:
            count += xor & 1
            xor >>= 1
        return count

    @staticmethod
    def minBitFlipsAnotherSolution(self, start: int, goal: int) -> int:

        count = 0
        # 1010 == 10
        #  ^
        # 0111 == 7
        # =
        # 1101 == 13

        while start != 0 or goal != 0:
            x, y = start & 1, goal & 1
            if x != y:
                count += 1

            start >>= 1
            goal >>= 1

        return count


if __name__ == "__main__":
    result = Solution.minBitFlips(self=Solution, start=10, goal=7)
    print(result)
