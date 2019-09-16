n, c = map(int, input().split())
p = sum(list(map(int, input().split())))

if (p / (n + 1)).is_integer():
    print(int(p / (n + 1)))
else:
    print(int(p / (n + 1) + 1))
