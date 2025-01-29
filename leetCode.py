a = int(input())
b = 0
T = False
while 2**b <= a:
    c = 2**b
    if c == a:
        T = True
        break
    b += 1
print(T)