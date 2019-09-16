a, b, x = (int(x) for x in input().split())
water_1l = int(x / 1000)    #買う１リットルのボトル数

a = min(a, b * 2)   #1L1本より500mL2本の方が安いならそっちを代入

if x - (1000 * water_1l) <= 500:
    print((a * water_1l) + b)
else:
    if 2 * b > a:
        print((a * (water_1l + 1)))
    else:
        print((a * (water_1l + 1) + (2 * b)))
