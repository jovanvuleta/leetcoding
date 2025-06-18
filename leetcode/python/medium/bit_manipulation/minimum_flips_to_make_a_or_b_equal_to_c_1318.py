class Solution:
    @staticmethod
    def minFlips(self, a: int, b: int, c: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        count = 0
        while a != 0 or b != 0 or c != 0:
            x, y, z = a & 1, b & 1, c & 1
            if x | y != z:
                if x == 1 and y == 1:
                    count += 2
                else:
                    count += 1

            a >>= 1
            b >>= 1
            c >>= 1
        return count


if __name__ == "__main__":
    result = Solution.minFlips(self=Solution, a=2, b=4, c=5)
    # 2 -> 0010
    # 4 -> 0110
    # 5 -> 0101
    print(result)
