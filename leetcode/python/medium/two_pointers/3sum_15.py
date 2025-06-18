class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == 0:
                    res.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif s < 0:
                    lo += 1
                else:
                    hi -= 1
        return res