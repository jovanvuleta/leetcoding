from typing import List


class Solution:
    @staticmethod
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """
            Time complexity: O(N * M * 2^N)
            Space complexity: O(2^N * N)
        """
        n = len(req_skills)

        # {"java": 0, "nodejs": 1, "reactjs": 2} -> track skill indexes in the array
        # (which are used for bit manipulation)
        index_dict = {skill: i for i, skill in enumerate(req_skills)}

        dp = {0: []}

        for i, p in enumerate(people):
            people_skill = 0
            for skill in p:
                # Joining person set of skills into one via OR bitwise operation
                # We shift it to left, as many times as the index of the current skill requires
                # e.q: a person knows reactjs and nodejs -> 110
                people_skill |= 1 << index_dict[skill]

            for pre_skills, team in list(dp.items()):
                updated_skills = people_skill | pre_skills

                if updated_skills == pre_skills:
                    continue

                if updated_skills not in dp or len(dp[updated_skills]) > len(team) + 1:
                    dp[updated_skills] = team + [i]

        return dp[(1 << n) - 1]


if __name__ == "__main__":
    print(Solution.smallestSufficientTeam(
        self=Solution,
        req_skills=["java", "nodejs", "reactjs"],
        people=[["java"], ["nodejs"], ["nodejs", "reactjs"]])
    )
