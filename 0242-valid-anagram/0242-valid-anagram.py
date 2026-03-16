class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        count_t = defaultdict(int)
        count_s = defaultdict(int)
        for i in t:
            count_t[i] += 1

        for i in s:
            count_s[i] += 1
        print(count_t, count_s)
        return count_t == count_s

        