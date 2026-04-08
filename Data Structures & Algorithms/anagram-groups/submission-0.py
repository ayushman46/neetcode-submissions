class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for s in strs:
            sorteds=''.join(sorted(s))
            if sorteds in res:
                res[sorteds].append(s)
            else:
                res[sorteds]=[s]
        return list(res.values())