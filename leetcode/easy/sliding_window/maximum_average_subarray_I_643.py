from typing import List


class Solution:
    @staticmethod
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        l, r = 0, k
        window_sum = sum(nums[l:r])
        max_avg = sum(nums[l:r]) / k

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, window_sum / k)

        return max_avg


if __name__ == "__main__":
    print(Solution.findMaxAverage(self=Solution, nums=[0, 1, 1, 3, 3], k=4))
