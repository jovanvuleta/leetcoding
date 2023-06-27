import heapq
import math
from heapq import heapify
from io import StringIO
from typing import List


class Solution:

    @staticmethod
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
            Time complexity: O(K)
            Space complexity: O(K)
        """
        if not nums1 or not nums2 or k == 0:
            return []

        minheap = [(nums1[0] + nums2[0], 0, 0)]  # (sum, i, j)
        visited = set()

        res = []
        while len(res) < k and minheap:
            # remove smallest (sum) from heap
            cur_sum, i, j = heapq.heappop(minheap)

            # add the current PAIR to result
            res.append([nums1[i], nums2[j]])

            # move i along nums1
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(minheap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            # move j along nums2
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(minheap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return res

    @staticmethod
    def show_tree(self, tree, total_width=60, fill=' '):
        """Pretty-print a tree.
        total_width depends on your input size"""
        output = StringIO()
        last_row = -1
        for i, n in enumerate(tree):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print(output.getvalue())
        print('-' * total_width)
        return

    @staticmethod
    def kSmallestPairsSecond(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(max_heap) < k:
                    heapq.heappush(max_heap, (-(nums1[i] + nums2[j]), nums1[i], nums2[j]))
                else:
                    if nums1[i] + nums2[j] > -max_heap[0][0]:
                        break
                    else:
                        heapq.heappushpop(max_heap, (-(nums1[i] + nums2[j]), nums1[i], nums2[j]))

        self.show_tree(self=Solution, tree=max_heap)
        return [[first, second] for (_, first, second) in max_heap]


if __name__ == "__main__":
    print(Solution.kSmallestPairs(self=Solution, nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
