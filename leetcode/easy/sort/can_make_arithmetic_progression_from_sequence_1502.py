from typing import List


class Solution:
    @staticmethod
    def canMakeArithmeticProgression(arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(0, len(arr) - 1):
            if arr[i + 1] - arr[i] != diff:
                return False

        return True


if __name__ == "__main__":
    print(Solution.canMakeArithmeticProgression(arr=[3, 5, 1]))
