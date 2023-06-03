import collections
from typing import List


class Solution:
    @staticmethod
    def countPairs(deliciousness: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        res = 0
        freq = collections.defaultdict(int)
        for x in deliciousness:
            for k in range(22):
                res += freq[2 ** k - x]
            freq[x] += 1

        return res % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution.countPairs(deliciousness=[1, 3, 5, 7, 9]))
