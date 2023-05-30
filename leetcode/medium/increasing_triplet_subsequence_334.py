import sys
from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest_num = second_smallest_num = sys.maxsize

        for num in nums:
            if num <= smallest_num:
                smallest_num = num
            elif num <= second_smallest_num:
                second_smallest_num = num
            else:
                return True

        return False

    @staticmethod
    def increasingTripletDpSolution(self, nums: List[int]) -> bool:
        """
            Time complexity: O(N * log(n))
            Space complexity: O(N)
        """
        dp = []

        for num in nums:
            index = bisect_left(dp, num)

            if index < len(dp):
                dp[index] = num
            else:
                dp.append(num)

            if len(dp) > 2:
                return True

        return False


if __name__ == "__main__":
    print(Solution.increasingTripletDpSolution(self=Solution, nums=[2, 1, 5, 0, 4, 6]))
