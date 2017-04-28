count = int(input())
numbers = list(map(int, input().split()))
step = int(input())

lr = []
rl = [0] * count
max_val = []

k = count-step
for i in range(count):
    if i%step == 0:
        lr.append(numbers[i])
    else:
        lr.append(max(lr[i-1], numbers[i]))


for i in range(count-1, -1, -1):
    if i == count-1:
        rl[i] = numbers[i]
    elif (i+1) % step == 0:
        rl[i] = numbers[i]
    else:
        rl[i] = (max(rl[i+1], numbers[i]))

for i in range(k+1):
    max_val.append(max(rl[i], lr[i+step-1]))

print(*max_val)
