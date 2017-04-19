def is_balanced(br):
    n = 0
    brackets = []
    for i in br:
        if i == '{' or i == '}' or i == '[' or i == ']' or i == '(' or i == ')':
            brackets.append(i)
    stack = []
    d = {}
    d['{'] = '}'
    d['('] = ')'
    d['['] = ']'
    if brackets[0] == ']' or brackets[0] == ')' or brackets[0] == '}' or len(brackets) % 2 != 0:
        return 1
    else:
        stack.append(brackets[0])
        for bracket in brackets[1:]:
            try:
                n+=1
                if bracket == d[stack[-1]]:
                    stack.remove(stack[-1])
            except IndexError:
                n+=1
        if len(stack) == 0:
            return 'Success'
        else:
            return n

br = input()
print(is_balanced(br))
