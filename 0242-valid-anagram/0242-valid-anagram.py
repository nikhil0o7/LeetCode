class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            return False
        count_t = Counter(t)
        count_s = Counter(s)
        return count_t == count_s

        