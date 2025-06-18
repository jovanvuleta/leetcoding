from typing import List


class Solution:
    @staticmethod
    def numOfWays(self, nums: List[int]) -> int:
        """
            Best case time complexity: O(N log N)
            Worst case time complexity: O(N ^ 2)
            Space complexity: O(N) - recursive stack
        """
        mod = 10 ** 9 + 7

        def combination(nl, nr):
            return factorial[nl + nr] // factorial[nl] // factorial[nr]

        def ways(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = [num for num in arr if num < root]
            right = [num for num in arr if num > root]

            return ways(left) * ways(right) * combination(len(left), len(right))

        n = len(nums)
        factorial = [1] * n

        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        return (ways(nums) - 1) % mod


if __name__ == "__main__":
    print(Solution.numOfWays(self=Solution, nums=[3, 4, 5, 1, 2]))
