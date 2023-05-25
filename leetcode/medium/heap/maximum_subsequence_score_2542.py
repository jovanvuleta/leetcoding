import heapq
from typing import List


class Solution:
    @staticmethod
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
            Time complexity: O(N * long(n))
            Space complexity: O(O(k))
        """
        A = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        h, curr_sum, best_score = [], 0, 0

        for num1, num2 in A:
            heapq.heappush(h, num1)  # h is a min heap
            curr_sum += num1

            if len(h) > k:
                curr_sum -= heapq.heappop(h)

            if len(h) == k:
                best_score = max(best_score, curr_sum * num2)

        return best_score


if __name__ == "__main__":
    print(Solution.maxScore(self=Solution, nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3))
