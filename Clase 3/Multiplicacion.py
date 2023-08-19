def multiplicacion(n,m):
    if (m == 1):
        return n
    else:
        return (n + multiplicacion(n, m-1))

x = multiplicacion(2,5)
print ("el resultado es", x)