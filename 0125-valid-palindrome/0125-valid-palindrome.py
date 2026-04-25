class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^A-Z0-9a-z]','',s)
        l,r = 0, len(s) - 1
        s = s.lower()
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
        