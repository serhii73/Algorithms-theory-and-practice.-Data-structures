stack = []


def push(v):
    stack.append(int(v))

def pop():
    stack.pop()

def maximum(stack):
    global big
    big = max(stack)
    print(big)

def prBig():
    print(big)

q = int(input())
# q = 10
task = []
for i in range(q):
    z = input()
    task.append(z)
# task = ['push 1', 'push 1', 'push 1', "max", 'push 1', 'push 2', 'max', 'pop', 'push 1', 'max', 'max', 'max']

try:
    for idx, i in enumerate(task):
        if i == 'max' and task[idx+1] == 'max':
            i = 'ptintBig'
except IndexError:
    pass


for a in task:
    if a.split()[0] == "push":
            push(a.split()[1])
    elif a == 'printBig':
        prBig()
    elif a == "pop":
        pop()
    else:
        maximum(stack)


max_i = []
for idx, i in enumerate(task):
    if i == 'max':
        max_i.append(idx)

