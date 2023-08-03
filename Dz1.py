n = int(input(''))
count_o = 0
count_r = 0
for i in range(n):
    x = int(input())
    if x == 1:
        count_o += 1
    else:
        count_r += 1
if count_o < count_r:
    print(count_o)
else:
    print(count_r)
