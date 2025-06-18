class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        if len(s) == 1:
            return True

        while l < r:
            while l < r and s[l].isalnum() is False:
                l += 1
            while r > l and s[r].isalnum() is False:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
