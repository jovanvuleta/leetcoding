from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        mapper = defaultdict(int)
        count = 0

        for num in nums:
            wanted = k - num
            if wanted in mapper and mapper[wanted] > 0:
                mapper[wanted] -= 1
                count += 1
            else:
                mapper[num] += 1

        return count


if __name__ == "__main__":
    print(Solution.maxOperations(self=Solution, nums=[2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], k=3))
