class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            d[sorted_str].append(s)
        return list(d.values())
        