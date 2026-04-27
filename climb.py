n = int(input("Enter number of steps: "))

if n <= 2:
    print(n)
else:
    a = 1
    b = 2
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    print(b)
