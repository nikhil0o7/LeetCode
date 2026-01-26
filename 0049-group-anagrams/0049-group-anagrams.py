class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in d:
                d[sortedS].append(s)
            else:
                d[sortedS] = [s]

        return list(d.values())
