a = 1
b = 2
c = 997
bHolder = 2
theanswer = 0
while (c >= 335):
    while (b < c):
        if (a * a + b * b == c * c):
            theanswer = a * b * c
            c = 334
            break
        b = b + 1
        c = c - 1
    a = a + 1
    b = bHolder + 1
    bHolder = b
    c = 1000 - a - b
print(theanswer)
