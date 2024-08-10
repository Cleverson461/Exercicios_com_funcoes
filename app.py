# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplica(1, 2, 3, 4, 5)
print(multiplicacao)

def parOuImpar(num1):
    if num1 % 2 == 0:
        print(f'{num1} é par.')
    else:
        print(f'{num1} é ímpar.')
        
parOuImpar(2)
parOuImpar(3)
parOuImpar(15)
parOuImpar(16)