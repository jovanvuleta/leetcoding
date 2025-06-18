from typing import List


class Solution:
    @staticmethod
    def putMarbles(weights: List[int], k: int) -> int:
        p = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)])
        return sum(p[len(p) - k + 1:]) - sum(p[:k - 1])


if __name__ == "__main__":
    print(Solution.putMarbles(weights=[1, 3, 5, 1], k=2))
