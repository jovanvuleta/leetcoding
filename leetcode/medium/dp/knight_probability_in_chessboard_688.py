class Solution:
    @staticmethod
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        """
            Time complexity: O(N^2 * M) - number of inputs * time per input
            Space complexity: O(N^2 * M)
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
