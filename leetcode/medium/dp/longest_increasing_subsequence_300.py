from bisect import bisect_left
from typing import List


class Solution:
    @staticmethod
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
            Time complexity: O(N * log(N))
            Space complexity: O(N)
        """

        arr = [nums.pop(0)]

        for n in nums:

            if n > arr[-1]:
                arr.append(n)
            else:
                index = bisect_left(arr, n)
                arr[index] = n

        return len(arr)

    @staticmethod
    def lengthOfLISSecond(self, nums: List[int]) -> int:
        """
            Time complexity: O(N^2)
            Space complexity: O(N)
        """
        cache = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    cache[i] = max(cache[i], 1 + cache[j])
        return max(cache)


if __name__ == "__main__":
    print(Solution.lengthOfLIS(self=Solution, nums=[1, 2, 4, 3]))
