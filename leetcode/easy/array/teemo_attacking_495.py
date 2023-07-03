from typing import List


class Solution:

    @staticmethod
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration

    @staticmethod
    def findPoisonedDurationSecond(self, timeSeries: List[int], duration: int) -> int:
        res = duration

        for i in range(1, len(timeSeries)):
            prev_time = timeSeries[i - 1]
            prev_duration = duration + prev_time - 1
            curr_time = timeSeries[i]
            curr_duration = timeSeries[i] + duration - 1

            if prev_duration >= curr_time:
                res += curr_duration - prev_duration
            else:
                res += duration

        return res


if __name__ == "__main__":
    print(Solution.findPoisonedDuration(self=Solution, timeSeries=[1, 3, 5, 7, 9, 11, 13, 15], duration=1))
