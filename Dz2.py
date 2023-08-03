def f(s, p):
    for i in range(s + 1):
        for j in range(s + 1):
            if i + j == s and i * j == p:
                return i, j

s = int(input())
p = int(input())
print(f(s, p))
