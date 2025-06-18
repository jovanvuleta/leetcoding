from typing import List


class Solution:

    @staticmethod
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = 2 * k + 1

        left = 0
        curr_sum = 0
        ans = [-1] * len(nums)
        for right in range(len(nums)):
            curr_sum += nums[right]

            if right - left + 1 >= n:
                ans[(right + left) // 2] = curr_sum // n
                curr_sum -= nums[left]
                left += 1

        return ans

    @staticmethod
    def getAveragesSecond(self, nums: List[int], k: int) -> List[int]:
        """
            Time complexity: O(N)
            Space complexity: O(N)
        """
        averages = [-1 for _ in nums]
        window_sum = sum(nums[0: 2 * k])

        for i in range(k, len(nums), 1):
            if i - k < 0:
                averages[i] = -1
                continue
            elif i + k > len(nums) - 1:
                break

            window_sum += nums[i + k]
            averages[i] = window_sum // (2 * k + 1)
            window_sum -= nums[i - k]

        return averages


if __name__ == "__main__":
    print(Solution.getAverages(self=Solution, nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
