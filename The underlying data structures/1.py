def isBalanced(br):
    brackets = []
    stack = []
    for i in br:
        if i == '{' or i == '}' or i == '[' or i == ']' or i == '(' or i == ')':
            brackets.append(i)

    len_our_brackets = [i for i in range(len(brackets))]
    d = {}
    for bracket, len_our_bracket in zip(brackets, len_our_brackets):
        d.setdefault(bracket, []).append(len_our_bracket)
    if brackets[0] == ']' or brackets[0] == ')' or brackets[0] == '}':
        return 1
    else:
        for our_bracket in brackets:
            if our_bracket == '{' or our_bracket == '[' or our_bracket == '(':
                stack.append(our_bracket)
            else:
                if len(stack) == 0:
                    return len(brackets)
                try:
                    if stack[-1] == '{' and our_bracket == '}' or stack[-1] == '(' \
                            and our_bracket == ')' or stack[-1] == '[' and our_bracket == ']':
                        stack.pop()
                    else:
                        stack.append(our_bracket)
                except:
                    pass

    # print(stack)
    # print(d)
    if len(stack) == 0:
        return "Success"
    else:
        for i in stack:
            # print('i: ', i)
            if i == '}' or i == ')' or i == ']':
                return d[i][-1]+1
            else:
                return len(brackets)


b = input()
a = isBalanced(b)
print(a)