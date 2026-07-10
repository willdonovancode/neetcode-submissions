class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict={}
        for i in range(0,len(nums)):
            numDict[nums[i]]=i
        for i in range(0,len(nums)):
            goal = target-nums[i]
            if goal in numDict and numDict[goal] != i:
                return [i,numDict[goal]]