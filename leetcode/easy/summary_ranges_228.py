from typing import List


class Solution:
    @staticmethod
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
            Time complexity: O(N)
            Space complexity: O(1)
        """
        if not nums:
            return []

        res = []
        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start != end:
                    res.append(f"{start}->{end}")
                else:
                    res.append(str(start))
                start = nums[i]
                end = nums[i]

        if start != end:
            res.append(f"{start}->{end}")
        else:
            res.append(str(start))

        return res


if __name__ == "__main__":
    print(Solution.summaryRanges(self=Solution, nums=[0, 2, 3, 4, 6, 8, 9]))
