class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        words=defaultdict(list)
        for s in strs:
            char="".join(sorted(s))
            words[char].append(s)

        res=[]

        for key,value in words.items():
            res.append(value)

        return res
            