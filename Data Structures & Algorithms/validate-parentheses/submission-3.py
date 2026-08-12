class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        if len(s)%2!=0:
            return False

        brackets={
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for char in s:
            if char in brackets and stack:
                if brackets[char]!=stack.pop():
                    return False
            else:
                stack.append(char)
            print(stack)
        return not stack
        