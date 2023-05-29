from typing import List


class Solution:
    @staticmethod
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        maxCandy = max(candies)
        res = [candy + extraCandies >= maxCandy for candy in candies]
        return res


if __name__ == "__main__":
    print(Solution.kidsWithCandies(self=Solution, candies=[2, 3, 5, 1, 3], extraCandies=3))
