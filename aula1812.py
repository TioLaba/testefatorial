#algoritmos interessantes

#recursividade
def fatorial_recursivo(n):
    if n > 1:
        fat = n * fatorial_recursivo(n - 1)
        return fat
    else:
        return 1

print(f'{3}! = {fatorial_recursivo(3)}')

