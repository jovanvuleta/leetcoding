import heapq
from typing import List


class KthLargest:
    """
        Heap pop - log(n)
        Heap initialization - O(N)
        Heap insertion - log(n)
        Binary tree insertion - O(N)

        Time complexity: O((N - k) * log(n)) - N-k is the number of popping operation done on the array,
        log(n) is the pop operation itself.
        Space complexity: O(N)
    """
    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    obj = KthLargest(3, [4, 5, 8, 2])
    obj.add(3)
    obj.add(5)
    obj.add(10)
    obj.add(9)
    obj.add(4)
