q = int(input())
stack = []

def push(v):
    stack.append(int(v))

def pop():
    stack.pop()


def max(stack):
    # this function fails if the list length is 0
    maximum = stack[0]
    for i in stack[1:]:
        if i > maximum: maximum = i
    print(maximum)

for i in range(q):
    a = input()
    if a.split()[0] == "push":
        push(a.split()[1])
    elif a == "pop":
        pop()
    else:
        max(stack)