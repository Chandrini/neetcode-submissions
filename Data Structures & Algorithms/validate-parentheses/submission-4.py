class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        closeopen={")":"(","}":"{","]":"["}

        for c in s:
            if c in closeopen:
                if stk and stk[-1]==closeopen[c]:
                    stk.pop()
                
                else:
                    return False
            else:
                stk.append(c)
        if stk==[]:
            return True
        else:
            return False