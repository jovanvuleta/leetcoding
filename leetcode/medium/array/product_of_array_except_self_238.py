from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            Time complexity: O(N)
            Space complexity: O(1) - output list is not considered additional space, it was stated in the question
        """
        res = []
        prefix = 1
        postfix = 1

        for i in range(0, len(nums)):
            res.append(prefix)
            prefix = prefix * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix = postfix * nums[i]

        return res


if __name__ == "__main__":
    print(Solution.productExceptSelf(self=Solution, nums=[1, 2, 3]))
