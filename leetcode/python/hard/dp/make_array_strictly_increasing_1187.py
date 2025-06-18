import bisect
from typing import List


class Solution:
    @staticmethod
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
            Time complexity: O(N * M * log(M))
            Space complexity: O(M) - len(arr)
        """
        dp = {-1: 0}
        arr2.sort()

        for num1 in arr1:
            new_dp = {}
            for key in dp:
                if num1 > key:
                    new_dp[num1] = min(new_dp.get(num1, float('inf')), dp[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    new_dp[arr2[loc]] = min(new_dp.get(arr2[loc], float('inf')), dp[key] + 1)
            dp = new_dp
            print(dp)

        if dp:
            return min(dp.values())
        return -1


if __name__ == "__main__":
    print(Solution.makeArrayIncreasing(self=Solution, arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]))
