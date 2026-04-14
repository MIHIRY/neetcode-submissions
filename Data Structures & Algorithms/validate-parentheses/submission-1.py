class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # closedToOpen = {"}" : "{", ")" : "(","]" : "["}

        # for i in s:
        #     if i in closedToOpen:
        #         if stack and stack[-1] == closedToOpen[i]:
        #             stack.pop()
                
        #         else:
        #             return False
        #     else:
        #         stack.append(i)
        
        # return True if not stack else False 

        stack = []
        hashmap = {"}" : "{", ")" : "(","]" : "["}

        for ch in s:
            if ch not in hashmap:
                stack.append(ch)
            
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[ch]:
                        return False
        return not stack