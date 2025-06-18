class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_num = float('inf')
        res = 0

        for price in prices:
            if price < min_num:
                min_num = price
            else:
                res = max(res, price - min_num)
        return res

