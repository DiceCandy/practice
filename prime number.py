a = 1
while a <= 50:
    a += 1
    b = 0
    while a - b > 1:
        b += 1
        if a % (a-b) == 0:
            break
    if a-b == 1:
        print(a)