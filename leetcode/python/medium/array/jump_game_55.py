class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = {n - 1: True}

        def can_reach(i):
            if i in memo:
                return memo[i]

            for jump in range(1, nums[i] + 1):
                if can_reach(i + jump):
                    return True

            return False

        return can_reach(0)

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        target = n - 1

        for i in range(n - 1, -1, -1):
            max_jump = nums[i]
            if i + max_jump >= target:
                target = i
        return target == 0


