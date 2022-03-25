# https://leetcode.com/problems/valid-parentheses/

# Use hashmap (dictionary) to store the opening & closing brackets
# Use stack for opening brackets

# Iterate through the string
# If opening bracket, append it to the stack
# Else if it’s the closing bracket and the stack is empty(meaning there is no opening bracket) or opening bracket doesn't match, return False
# Finally check if the stack still contains unmatched left bracket

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for c in s:
            if c in bracket:
                stack.append(c) #only opening brackets are appended 
            elif not stack or bracket[stack.pop()] != c:
                return False
        
        #stack should be empty since all opening and closing brackets should match
        return not stack

