class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)-1
        nums.sort()
        res=[]

        for i in range(n+1):
            if i>0 and nums[i]==nums[i-1]:
                continue #goes to next iteration

            l=i+1
            r=n

            while l<r:
                added=[nums[i],nums[l],nums[r]]
                if sum(added)>0:
                    r-=1
                elif sum(added)<0:
                    l+=1
                else:
                    res.append(added)
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res




             