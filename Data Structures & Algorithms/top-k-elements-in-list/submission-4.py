class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        frequency=defaultdict(int)

        for n in nums:
            frequency[n]+=1
        
        res=[]

        #brute force

        sorted_freq=dict(sorted(frequency.items(), key=lambda item: item[1],reverse=True))

        i=0
        for key,val in sorted_freq.items():
            res.append(key)
            i+=1
            if i==k:
                return res