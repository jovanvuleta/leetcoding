from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    1. Two Sum
        Solution: Populate the set with the elements in the list and its index, and constantly check if you have a
        number difference from the total sum number and the current iterative number. If so return their indexes.
        Time complexity: O(N)
        Space complexity: O(N)
    """
    res = {}
    for i in range(len(nums)):
        if target - nums[i] in res:
            return [res[target - nums[i]], i]
        res[nums[i]] = i
    return []


if __name__ == "__main__":
    test_list = [1, 3, 4, 2]
    target_number = 6
    result = twoSum(test_list, target_number)
    print(result)
