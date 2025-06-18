class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        m1, m2 = {}, {}

        arr = s.split(" ")

        if len(pattern) != len(arr):
            return False

        for c, w in zip(pattern, arr):
            if (c in m1 and m1[c] != w) or (w in m2 and m2[w] != c):
                return False
            m1[c], m2[w] = w, c
        return True
