from typing import List


class Solution:
    @staticmethod
    def minimizeMax(nums: List[int], p: int) -> int:
        """
            Time complexity: O(N * log(M))
            Space complexity: O(1)
        """

        def is_valid(threshold):
            # Greedy
            i, cnt = 0, 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False

        if p == 0:
            return 0

        nums.sort()
        l, r = 0, max(nums) - min(nums)  # upper value of the binary search is bounded by the max - min value diff
        res = 10 ** 9

        while l <= r:
            m = l + (r - l) // 2
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res


if __name__ == "__main__":
    print(Solution.minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))
