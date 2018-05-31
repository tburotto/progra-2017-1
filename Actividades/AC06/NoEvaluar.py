def numeros():
    a = 0
    while True:
        yield a
        a += 1

numeros = numeros()
print(next(numeros))
print(next(numeros))
print(next(numeros))
