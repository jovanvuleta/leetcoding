from typing import List


class Solution:
    @staticmethod
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
            Time complexity: O(k * N^k)
            Space complexity: O(k * N^k)
        """

        def backtrack(start, comb):
            if len(comb) == k:
                # res.append(comb.copy())
                res.append(comb[:])
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()

        res = []
        backtrack(1, [])
        return res


if __name__ == "__main__":
    print(Solution.combine(self=Solution, n=4, k=2))
