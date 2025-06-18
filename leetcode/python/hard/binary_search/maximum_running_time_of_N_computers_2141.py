from typing import List


class Solution:
    @staticmethod
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
            Intuition: Finding the lower and upper bound of the battery range, for binary search usage.
            Time complexity: O(N * log(N))
            Space complexity: O(1)
        """

        def can_fit(time_span):
            target_bat_sum, curr_bat_sum = n * time_span, 0

            for bat in batteries:
                curr_bat_sum += min(time_span, bat)
                if curr_bat_sum >= target_bat_sum:
                    return True

            return curr_bat_sum >= target_bat_sum

        l, r = min(batteries), sum(batteries) // n + 1
        ans = -1

        while l < r:
            m = (l + r) // 2
            if can_fit(m):
                ans = m
                l = m + 1
            else:
                r = m

        return ans

    @staticmethod
    def maxRunTimeSecond(n: int, batteries: List[int]) -> int:
        """
            Intuition: Greedy
            Time complexity: O(N * log(N))
            Space complexity: O(1)
        """
        batteries.sort()
        total = sum(batteries)
        while batteries[-1] > total // n:
            n -= 1
            total -= batteries.pop()
        return total // n


if __name__ == "__main__":
    print(Solution.maxRunTime(self=Solution, n=2, batteries=[3, 3, 3]))
    # print(Solution.maxRunTimeSecond(self=Solution, n=3, batteries=[10, 10, 3, 5]))
