class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        for i in range(0,len(s)):
            temp=list(s)
            # r=list(reversed(temp))
            # toRemove=temp.pop(i)
            # r.remove(toRemove)
            temp.pop(i)
            r=list(reversed(temp))
            if temp==r:
                return True


        return False