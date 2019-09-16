import sys

n = int(input())
a = list(map(int, input().split()))
q = int(input())
xy = []

for i in range(q): 
    #各命令を２次元配列としてxyに格納
    xy_i = list(map(int, input().split()))
    xy.append(xy_i)

if sorted(a) == a:
    #最初から昇順の場合は０を出力しプログラムを終了
    print(0)
    sys.exit()

for i in xy:
    a[i[0] - 1], a[i[1] - 1] = a[i[1] - 1], a[i[0] - 1] #2値入れ替え
    if sorted(a) == a:
        #昇順だった場合その場所を出力してプログラム終了
        print(xy.index(i) + 1)
        sys.exit()

if sorted(a) != a:
    #どの命令を実行しても昇順にならなかった場合-1を実行
    print(-1)
