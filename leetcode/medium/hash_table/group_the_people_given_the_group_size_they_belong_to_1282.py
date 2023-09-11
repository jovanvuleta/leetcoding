from typing import List


class Solution:
    @staticmethod
    def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []

        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)

            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result


if __name__ == "__main__":
    print(Solution.groupThePeople(groupSizes=[3, 3, 3, 3, 3, 1, 3]))
