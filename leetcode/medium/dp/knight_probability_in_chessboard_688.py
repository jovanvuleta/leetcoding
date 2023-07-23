class Solution:

    @staticmethod
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
            Intuition: Top-down dp approach, where we are starting from the knight starting pos, and calculating the
            probability positions from there.
            Time complexity: O(N^2 * K) - number of inputs * time per input
            Space complexity: O(N^2 * K)
        """
        def dp(cur_k, cur_r, cur_c):
            if (cur_k, cur_r, cur_c) in memo:
                return memo[(cur_k, cur_r, cur_c)]

            if cur_k == k:
                return 1

            ans = 0

            for d in moves:
                new_r = cur_r + d[0]
                new_c = cur_c + d[1]

                if 0 <= new_r < n and 0 <= new_c < n:
                    ans += 0.125 * dp(cur_k + 1, new_r, new_c)  # 1 / 8(possible moves by knight) == 0.125

            memo[(cur_k, cur_r, cur_c)] = ans

            return ans

        memo = {}
        moves = ((2, 1), (-2, -1), (-2, 1), (2, -1), (1, 2), (-1, -2), (-1, 2), (1, -2))

        return dp(0, row, column)


    @staticmethod
    def knightProbabilitySecond(self, n: int, k: int, row: int, column: int) -> float:
        """
            Intuition: Bottom-up dp approach, where we are checking all positions in the grid that lead to the start pos
            Time complexity: O(N^2 * K) - number of inputs * time per input
            Space complexity: O(N^2 * K)
        """
        knight_moves = [(2, 1), (-2, -1), (-2, 1), (2, -1), (1, 2), (-1, -2), (-1, 2), (1, -2)]
        cache = [[[None] * (k + 1) for _ in range(n)] for _ in range(n)]
        has_cache = [[[False] * (k + 1) for _ in range(n)] for _ in range(n)]

        def p(r, c, k):
            if k == 0:
                if r == row and c == column:
                    return 1.0
                else:
                    return 0.0

            total_probability = 0.0

            if has_cache[r][c][k]:
                return cache[r][c][k]

            for dr, dc in knight_moves:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    total_probability += p(nr, nc, k - 1)

            has_cache[r][c][k] = True
            cache[r][c][k] = total_probability / 8.
            return cache[r][c][k]

        total_probability = 0.0
        for r in range(n):
            for c in range(n):
                total_probability += p(r, c, k)
        return total_probability


if __name__ == "__main__":
    print(Solution.knightProbability(self=Solution, n=3, k=2, row=0, column=0))
