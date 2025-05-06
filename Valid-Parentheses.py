#utilize a stack(first in last out), create a hashmap where open brackets as key, closing brackets as value
#iterate through the string:
#   if it's a open bracket, push it to the stack
#   else: if the stack is empty or the closing doesn't match with the value in hashmap. return false
#in the end, return True

class Solution:
    def isValid(self, s: str) -> bool:
        matches = {'(': ')', '{': '}', '[' : ']'}
        stack = [] 
        
        for bracket in s:
            if bracket in matches: stack.append(bracket)
            else:
                if stack: last_open_bracket = stack[-1]
                if not stack or bracket != matches[last_open_bracket]: return False
                else: stack.pop()

                
        return True if not stack else False
        