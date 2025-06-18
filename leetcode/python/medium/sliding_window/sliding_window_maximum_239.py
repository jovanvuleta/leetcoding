from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        """
            Intuition: Monotonic stack
            Time complexity: O(N)
            Space complexity: O(N)
        """
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output


if __name__ == "__main__":
    print(Solution.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
