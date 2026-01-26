from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = Counter(s)
        countT = Counter(t)

        for k,v in Counter.items(countT):
            if v != countS.get(k, 0):
                return False
        return True
