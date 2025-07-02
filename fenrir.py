def isValid(s: str) -> bool:
    stack = [] # ({[を記録

    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.append(char) # ({[を追加

        #)}]の場合直前の({[が直前にあるか確認
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif char == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()

    # stackが空だった場合true
    if stack:
        return False
    else:
        return True

# test
s = '()'
print(isValid(s)) # True
s = '({)}'
print(isValid(s)) # False
