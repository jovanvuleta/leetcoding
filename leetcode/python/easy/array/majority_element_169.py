class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n

            if n == res:
                count += 1
            else:
                count -= 1
        return res

