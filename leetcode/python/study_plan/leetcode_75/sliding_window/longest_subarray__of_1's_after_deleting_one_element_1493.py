from typing import List


class Solution:

    @staticmethod
    def longestSubarray(nums: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        l = r = k = 0
        best = 0

        while r < len(nums):
            if nums[r] == 0:
                k += 1
            while k > 1:
                if nums[l] == 0:
                    k -= 1
                l += 1
            r += 1
            best = max(best, r - l - 1)

        return best

    @staticmethod
    def longestSubarrayFourth(self, nums: List[int]) -> int:
        ans = sum = lo = 0
        for hi, num in enumerate(nums):
            sum += num
            if sum < hi - lo:
                sum -= nums[lo]
                lo += 1
            ans = max(ans, hi - lo)
        return ans

    @staticmethod
    def longestSubarrayThird(nums: List[int]) -> int:
        max_length, left, count_zero = 0, 0, 0

        for right in range(len(nums)):
            count_zero += nums[right] == 0
            if count_zero > 1:
                count_zero -= nums[left] == 0
                left += 1
            max_length = max(max_length, right - left)
        return max_length

    @staticmethod
    def longestSubarraySecond(nums: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        l, r, count, k = 0, 0, 0, 1

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l


if __name__ == "__main__":
    result = Solution.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1])
