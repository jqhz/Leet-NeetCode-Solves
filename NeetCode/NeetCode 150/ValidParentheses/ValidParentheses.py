class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = { ")":"(", "]":"[","}":"{"}
        for char in s:
            if char in mappings:
                if stack and stack[-1]==mappings[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
    
# Stack implementation 
'''
1. create stack and map each closing to each opening
2. for each parenthesis
    if opening
        add to stack
    if closing
        check if stack exists
        if last element in stack is the complement to closing parenthesis
            pop from stack
    true if stack is empty
    else false since not every parenthesis is closed

'''