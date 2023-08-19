def division (n, m):
    if (n < m):
        return 0
    else:
        return 1 + division(n-m, m)

x = division(9, 3)
print ("el resultado es", x)