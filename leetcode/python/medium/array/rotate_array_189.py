class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # handle k > len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[(i + k) % n] = nums[i]

        for i in range(n):
            nums[i] = res[i]
