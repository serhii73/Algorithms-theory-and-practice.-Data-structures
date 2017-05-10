n = int(input())

d = {}

tasks = []
for i in range(n):
    query = input()
    tasks.append(query)

for a in tasks:
    if 'add' == a.split()[0]:
        try:
            d[int(a.split()[1])] = a.split()[2]
        except KeyError:
            pass
    elif 'find' == a.split()[0]:
        try:
            print(d[int(a.split()[1])])
        except KeyError:
            print("not found")
    elif 'del' == a.split()[0]:
        try:
            d.pop(int(a.split()[1]))
        except KeyError:
            pass