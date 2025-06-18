class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r = 0, n - 1

        res = float('-inf')

        while l < r:
            width = r - l
            res = max(res, width * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
