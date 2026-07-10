class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        mymap=defaultdict(int)
        for i in range(0,len(nums)):
            goal=target-nums[i]
            if goal in mymap.keys():
                return [mymap[goal],i]
            else:
                mymap[nums[i]]=i
        return [-1,-1]