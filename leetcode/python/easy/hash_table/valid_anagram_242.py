from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = Counter(s)

        for v in t:
            if v not in m:
                return False
            m[v] -= 1
            if m[v] == 0:
                del m[v]

        return len(m) == 0
