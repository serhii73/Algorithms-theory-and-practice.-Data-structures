stack = []
stack_max = []

def push(v):
    stack.append(int(v))

def pop():
    stack.pop()
    stack_max.pop()

q = int(input())
task = []
for i in range(q):
    z = input()
    task.append(z)


for a in task:
    if a.split()[0] == "push":
        push(a.split()[1])
        try:
            if int(stack_max[-1]) <= int(a.split()[1]):
                stack_max.append(int(a.split()[1]))
            else:
                stack_max.append(stack_max[-1])
        except IndexError:
            stack_max.append(stack[-1])
    elif a == "pop":
        pop()
    else:
        print(stack_max[-1])
