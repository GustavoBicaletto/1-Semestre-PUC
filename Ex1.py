# 1 - Elabore uma função que dado um número inteiro ela imprima o seu sucessor e antecessor

    # control + 2 pontos = comentario

'''def numero(numero_selec):    
    print(f'O antecessor de {numero_selec} é {numero_selec-1}')
    print(f'O sucessor de {numero_selec} é {numero_selec+1}')

x = int(input('Digite um número: '))
numero(x) 

def numero():    
    x = int(input('Digite um número: '))
    print(f'O antecessor de {x} é {x-1}')
    print(f'O sucessor de {x} é {x+1}')
    
numero()  '''

# JEITOS DIFERENTES PRO MESMO RESULTADO

''' 2 - Elabore um programa que possua duas funções:
• Uma função que leia um número inteiro
• Uma função que some três valores inteiros
• O programa deverá ler três valores inteiros e imprimir a soma
desses valores, usando as funções acima '''

'''def numero_int():
    x = int(input('Digite um numero inteiro: '))
    return x

resultado = numero_int()
print(resultado)'''

# TODA FUNÇÃO TEM UM RETURN

def numero_int(): 
    numero = int(input('Digite um numero inteiro: '))
    print(numero)
    return numero

def tres_int(a,b,c):
    soma = a+b+c
    return soma

a = numero_int()
b = numero_int()
c = numero_int()

soma = tres_int(a,b,c)
print(soma)

# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o
# custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

