class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
              

        for char in s :
            ## checks if the character is opening bracket
            if char in "[{(":
                stack.append(char)
            else:
                 if not stack: 
                    return False
                 opening = stack.pop()

                # Check whether brackets match
                 if opening != pairs[char]:
                    return False
        return len(stack)==0  