class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = r = 0

        while r < len(nums):
            count = 0
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                count += 1
                r += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i

    def removeDuplicates3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = r = 1
        count = 1

        while r < len(nums):
            if nums[r] == nums[r - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[l] = nums[r]
                l += 1
        return l