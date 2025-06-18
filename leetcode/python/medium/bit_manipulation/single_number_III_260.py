from typing import List


class Solution:
    @staticmethod
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
            Intuition: x1 ^ x2 = xor
                First find xor of all number, then find the first bit of xor, and find the remaining x2.
            Time complexity: O(N)
            Space complexity: O(1)
        """
        xor = 0
        for n in nums:
            xor ^= n

        # Get the first rightmost bit
        # first_bit = xor & (xor - 1) ^ xor
        first_bit = xor & (-xor)

        num1 = 0
        for n in nums:
            if n & first_bit:  # if number contains the first bit of the xor
                num1 ^= n

        return [num1, num1 ^ xor]


if __name__ == "__main__":
    print(Solution.singleNumber(self=Solution, nums=[1, 2, 1, 3, 2, 5]))
