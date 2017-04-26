count = int(input())
numbers = list(map(int, input().split()))
step = int(input())
rezult = []
stack = []


for i in numbers[:step]:
    stack.append(i)


rezult.append(max(stack))

for i in numbers[step:]:
    stack.append(i)
    stack.pop(0)
    rezult.append(max(stack))

print(*rezult)
