from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        curr = []
        backtrack(curr)
        return ans

    def permuteThird(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(remaining, current):
            if not remaining:
                res.append(current[:])  # Make a copy of the current permutation
                return

            for i in range(len(remaining)):
                num = remaining[i]
                current.append(num)
                backtrack(remaining[:i] + remaining[i + 1:], current)  # Pass a copy of remaining list without i index
                current.pop()  # Remove the last element to backtrack and try other permutations

        backtrack(nums, [])
        return res

    def permuteSecond(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permuteSecond(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)

        return res


if __name__ == "__main__":
    a = Solution()
    print(a.permute(nums=[1, 2, 3]))
