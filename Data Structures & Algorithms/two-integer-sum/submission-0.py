class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers={}
        for i in range(0,len(nums)):
            goal=target-nums[i]
            if goal in numbers.keys():
                return [numbers[goal],i]
            else:
                numbers[nums[i]]=i
        