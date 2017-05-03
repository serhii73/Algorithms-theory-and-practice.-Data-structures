def is_balanced(our_line):
    """Correctly placed brackets?"""
    brackets = []
    stack = []
    for idx, i in enumerate(our_line):
        if i == '{' or i == '}' or i == '[' or i == ']' or i == '(' or i == ')':
            brackets.append([i, idx])

    if brackets[0][0] == ']' or brackets[0] == ')' or brackets[0] == '}':
        return 1
    else:
        for our_bracket in brackets:
            if our_bracket[0] == '{' or our_bracket[0] == '[' or our_bracket[0] == '(':
                stack.append(our_bracket)
            else:
                try:
                    if stack[-1][0] == '{' and our_bracket[0] == '}' or stack[-1][0] == '(' \
                            and our_bracket[0] == ')' or \
                            not (not stack[-1][0] == '[' or not our_bracket[0] == ']'):
                        stack.pop()
                    else:
                        stack.append(our_bracket)
                except IndexError:
                    stack.append(our_bracket)
    if len(stack) == 0:
        return "Success"
    else:
        for i in stack:
            if not (not (i[0] == '}') and not (i[0] == ')')) or i[0] == ']':
                return i[1]+1
    for i in stack:
        if i[0] == '{' or i[0] == '(' or i[0] == '[':
            return i[1] + 1


symbols_and_brackets = input()
rezult = is_balanced(symbols_and_brackets)
print(rezult)
