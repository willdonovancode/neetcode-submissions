class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        #longest substring with Same characters
        #aaxa k=1 replace x with a and return 4
        
        count=defaultdict(int)

        res=0
        l=0
        freq=0

        for r in range(len(s)):
            count[s[r]]+=1

            freq=max(freq,count[s[r]])

            #size of window - freq > max changes
            if (r-l+1)-freq>k:
                count[s[l]]-=1
                l+=1
            
            res=max(res,r-l+1)
        return res

        
        
