### TESTE DE FUNÇÕES ###

# Exemplo MUITO simples de função, serve para otimizar o programa e evitar repetições desnecessarias

def linha():                           #|
    print('-'*30)                      #|
    return                             #| # Crio a função uma vez e posso chamar ela sempre, desse jeito não preciso repetir as mesmas coisas, como abaixo:
                                       #|
# linha()                              #| print('-'*30) 
# print('Sistema de Alunos')           #| print('Sistema de Alunos')
# linha()                              #| print('-'*30) 
# print('Cadastro do Aluno')           #| print('Cadastro do Aluno') 
# linha()                              #| print('-'*30) 
# print('Erro do Sistema')             #| print('Erro do Sistema')
# linha()                              #| print('-'*30) 

# Em de vez de usar esse "print('-'*30)" repetidas vezes, eu criei uma função onde toda vez q chamo a função "linha()", essa linha é criada sem precisar
# Caso eu queira fazer uma linha usando outro caractere, basta eu usar um parametro e quando chamar a função usando "linha()" eu coloco o caractere dentro do parenteses:

'''def linha(carac):
    print(carac*30)
    return'''

# No exemplo abaixo, to usando a função q criei lá em cima dentro desse nova funçao "mensagem()". dessa vez criei um parâmetro pra essa funçao
# que é (msg), e coloquei dentro do print. Agora sempre q eu chamar essa funçao, eu preciso inserir algo nela e vai aparecer no lugar do print do inserido

def mensagem(msg):
    linha()
    print(msg)
    linha()
    return # AINDA TO TENTANDO DESCOBRIR A FUNÇÃO DO RETURN :(

# mensagem('Sistema de alunos')
# mensagem('Cadastro do Aluno')
# mensagem('Erro de Sistema')


#Exemplo de uma função conveninente, função de soma basica:

def soma(a,b):
    s = a + b
    print(s)


### DESAFIOS ###


''' Faça um programa que tenha uma função chamada área(), que receba as dimensõesde um terreno retangular(largura e comprimento) e mostre a área do terreno '''

def area(lar, comp):
    # largura = input(float('Digite a Largura do terreno: '))
    # comprimento = input(float('Digite o Comprimetno do terreno: '))
    área = lar * comp
    print(f'A área de um terreno {lar}x{comp} é de {área}metros quadrados')
    return


# mensagem('Cálculo de Área')
# area(5.5, 50)
# linha()

''' Faça um programa que tenha uma função escreva(), que receba um texto como parãmetro e mostre uma mensagem com tamanho adaptável '''

def escreva(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg))
    return

# escreva('Vasco da Gama')

''' Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem
Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
'''


def contador():
    print('De 1 até 10, 1 em 1 de passo')
    for t in range(1,11,1):
        print(t)
    linha()
    print('De 10 até 1, de 2 em 2')
    for s in range(10,1,-2):
        print(s)
    linha()
    i = int(input('Digite o ínicio: '))
    f = int(input('Digite o fim: '))
    p = int(input('Digite o passo: '))

    if p == 0:
        p = 1

    print(f'De {i} até {f}, de {p} em {p}')
    if i > f:
        p = p *-1
        f = f - 1
    elif i < f:
        f = f + 1
    for x in range(i,f,p):
        print(x)


''' Faça um programa que tenha uma lista chamada de números e duas funções chamadas sorteio() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior '''

numeros = []

def sorteio():
    import random
    while True:
        contador = 0
        resultado = random.randint(1,100)
        numeros.append(resultado)
        if resultado > 0:
            contador += 1
        elif contador == 5:
            break  
    
    print(numeros)

sorteio()
linha()


