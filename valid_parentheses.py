def is_valid(s):
    stack = []
    pairs = {")": "(", "]":"[", "}":"{"}
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False
            if stack.pop() != pairs[char]:
                return False
    return not stack
print(is_valid("()"))
print(is_valid("()[]"))
print(is_valid("[]"))
print(is_valid("(]"))
print(is_valid("([)]"))
