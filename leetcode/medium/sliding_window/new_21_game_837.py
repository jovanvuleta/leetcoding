class Solution:
    @staticmethod
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
            Question type: Sliding Window/DP question
            Time complexity: O(K + maxPts)
            Space complexity: O(K)
        """
        if k == 0:
            return 1.0

        window_sum = 0
        for i in range(k, k + maxPts):
            window_sum += 1 if i <= n else 0

        dp = {}

        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)
            window_sum += dp[i] - remove

        return dp[0]

    @staticmethod
    def new21GameDFSSolution(self, n: int, k: int, maxPts: int) -> float:
        cache = {}

        # Start at score, return the probability
        def dfs(score):
            if score >= k:
                return 1 if score <= n else 0
            if score in cache:
                return cache[score]

            prob = 0
            for i in range(1, maxPts + 1):
                prob += dfs(score + i)

            cache[score] = prob / maxPts
            return cache[score]

        return dfs(0)


if __name__ == "__main__":
    print(Solution.new21Game(self=Solution, n=1, k=2, maxPts=2))
