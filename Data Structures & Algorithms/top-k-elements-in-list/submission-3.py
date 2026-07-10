class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        count=defaultdict(int)

        for n in nums:
            count[n]+=1

        arr=[]

        for value,c in count.items():
            arr.append([c,value])
        arr.sort()

        res=[]

        while len(res)<k:
            res.append(arr.pop()[1])

        return res

        