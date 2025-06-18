from typing import List


class Solution:
    @staticmethod
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
            Time complexity: O(log(N))
            Space complexity: O(N)
        """
        l, r = 0, len(arr) - 1

        while l != r:
            m = (l + r) // 2
            if arr[m] > arr[m + 1]:
                r = m
            else:
                l = m + 1
        return l


if __name__ == "__main__":
    print(Solution.peakIndexInMountainArray(self=Solution, arr=[24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
