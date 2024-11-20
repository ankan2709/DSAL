def validParenthesis(string):
    stack = []
    closeToOpen = {')':'(', '}':'{', ']':'['}

    for char in string:
        if char in closeToOpen:
            if stack and stack[-1] == closeToOpen[char]:
                stack.pop()
            else:
                return False
            
        else:
            stack.append(char)
            
    if stack:
        return False
    else:
        return True

s = "()"
print(validParenthesis(s))
s = "()[]{}"
print(validParenthesis(s))
s = "(]"
print(validParenthesis(s))
s = "([])"
print(validParenthesis(s))