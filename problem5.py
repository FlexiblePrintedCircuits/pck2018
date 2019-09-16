a, n, m = (int(x) for x in input().split())
x = []

for i in range(m):
    i += 1
    y = sum(list(map(int, str(i)))) #一旦文字列化して各桁の和を求める
    if (y + a) ** n == i:
        x.append((y + a) ** n)

print(len(x))
