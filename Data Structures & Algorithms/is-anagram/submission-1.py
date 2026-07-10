class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s1=list(s)
        t=list(t)
        print(t)
        print(t.sort())
        return sorted(s1)==sorted(t)
        