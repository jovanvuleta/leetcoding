import heapq
from collections import Counter


class Solution:
    @staticmethod
    def reorganizeString(s: str) -> str:
        """
            Time complexity: O(N * log(N))
            Space complexity: O(len(s))
        """
        count = Counter(s)
        max_heap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(max_heap)  # O(N)

        prev = None
        res = ""
        while max_heap or prev:
            if prev and not max_heap:
                return ""

            cnt, char = heapq.heappop(max_heap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return res


if __name__ == "__main__":
    print(Solution.reorganizeString(s="aaab"))
