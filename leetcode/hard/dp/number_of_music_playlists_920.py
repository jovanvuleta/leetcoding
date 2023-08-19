class Solution:
    @staticmethod
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        """
            Time complexity: O(N * goal)
            Space complexity: O(N * goal)
        """
        mod = 10 ** 9 + 7
        dp = {}

        def count(cur_goal, old_songs):
            if cur_goal == 0 and old_songs == n:
                return 1
            if cur_goal == 0 or old_songs > n:
                return 0
            if (cur_goal, old_songs) in dp:
                return dp[(cur_goal, old_songs)]

            # Choose new song
            res = (n - old_songs) * count(cur_goal - 1, old_songs + 1)

            if old_songs > k:
                # Choose old song
                res += (old_songs - k) * count(cur_goal - 1, old_songs)
            dp[(cur_goal, old_songs)] = res % mod
            return dp[(cur_goal, old_songs)]

        return count(goal, 0)


if __name__ == "__main__":
    print(Solution.numMusicPlaylists(self=Solution, n=2, goal=3, k=1))
