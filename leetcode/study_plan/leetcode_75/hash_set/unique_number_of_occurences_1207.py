from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        set_size = set(count.values())

        return len(count) == len(set_size)

    @staticmethod
    def uniqueOccurrencesSecond(self, arr: List[int]) -> bool:
        dec = Counter(arr)
        return len(dec) == len(set(dec.values()))


if __name__ == "__main__":
    print(Solution.uniqueOccurrences(self=Solution, arr=[1, 2, 2, 1, 1, 3]))
