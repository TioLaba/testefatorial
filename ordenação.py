#algoritmos de ordenação

# Apresentação

#entrada
#num1 = 35
#num2 = 7
num = [-35, -7, -1024, -2]

#processamento
for i in range(0, len(num)-1):
    for j in range((i + 1), len(num)):
        if num[i] > num[j]:
             swap = num[j]       #swap é um espaço intermediario
             num[j] = num[i]
             num[i] = swap
#saida
#print(f'\n{num[0]}, {num[1]}, {num[2]}, {num[3]} \n')
#for n in num:
#    print(f'{n},' end='')
for i in range(0, len(num)):
    if i < len(num) - 1:
        print(f'{num[i]},', end = '')
    else:
        print(f'{num[i]}.')
