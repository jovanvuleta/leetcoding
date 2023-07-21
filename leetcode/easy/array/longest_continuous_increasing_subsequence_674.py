from typing import List


class Solution:
    @staticmethod
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        if len(nums) == 1:
            return 1

        prev = nums[0]
        res = count = 1

        for num in nums[1:]:
            count = count + 1 if prev < num else 1
            prev = num
            res = max(res, count)

        return res


if __name__ == "__main__":
    print(Solution.findLengthOfLCIS(self=Solution, nums=[1, 3, 5, 4, 2, 3, 4, 5]))
