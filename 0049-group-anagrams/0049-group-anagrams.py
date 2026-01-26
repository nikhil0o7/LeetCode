class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in d:
                d.append(sortedS)
            else:
                d[sortedS] = [s]

        return list(d.values())
