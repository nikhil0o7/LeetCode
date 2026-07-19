class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for st in strs:
            s = "".join(sorted(st))
            dic[s].append(st)

        return list(dic.values())
                
        