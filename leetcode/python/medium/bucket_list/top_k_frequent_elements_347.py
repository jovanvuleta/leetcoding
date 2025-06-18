from typing import List


class Solution:
    @staticmethod
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            Topics: Bucket list
            Solution: Storing the numbers in the bucket list indices which represent the number of
            occurrence of the number. List inside the index represent the numbers that occurred that many times.
            Time complexity: O(N)
            Space complexity: O(N)
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]  # + 1 because of the indexing done in the freq list

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    print(Solution.topKFrequent(self=Solution, nums=[1, 1, 1, 2, 2, 3], k=1))
