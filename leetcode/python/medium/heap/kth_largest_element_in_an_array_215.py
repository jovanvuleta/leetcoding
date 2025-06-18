import heapq
from typing import List


class Solution:
    def findKthLargest(nums: List[int], k: int) -> int:
        """
            Time complexity: O(N * log(k)) - log(k) are the heap operations
            Space complexity: O(k)
        """
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]


if __name__ == "__main__":
    print(Solution.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
