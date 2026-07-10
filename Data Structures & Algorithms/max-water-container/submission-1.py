class Solution:
    def maxArea(self, heights: List[int]) -> int:
        longest=0

        L=0
        R=len(heights)-1

        while L<R:
            total=min(heights[L],heights[R])
            mult=R-L
            total*=mult
            longest=max(total,longest)
            if heights[L]>heights[R]:
                R-=1
            else:
                L+=1
        
        return longest