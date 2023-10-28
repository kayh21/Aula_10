# Tuple = estrutura de dados, uma vez criada nao pode ser alterada e parece uma lista, exemplo: documentacao
# Tupla utiliza parenteses ()
# Listas utiliza chaves []
# Dicionario utiliza colchetes {}, dicionário é o JSON que guarda muitas listas de dados e códigos hash = dicts
#Exemplo de dicionario: 
# dictin = {'Key1': "value1",'Key2': "value2,........}
# Tupla tem o mesmo comportamento de uma constante 
# indice e a posicao do dado na memoria ROM com base de 2 elevado a n tambem chamado de INDEX = posicao do endereco do dado
# acessar indice print(tuple[0])
# converter tupla em lista utiliza-se: list()
# tuple = (1,2,3,4,5)
# x = list(tuple)
# print(x)
# Function none() significa def() em python:
# precisa-se identar o código que é organizar o código
# declara a palavra: def nome da função()
# nome da função precisa ser semantico, levando o nome do que faz
# usar parametros torna a funçao pura podendo alterar
# variavel local só pode ser usada dentro da função 
# variavel global pode ser usada em qualquer coisa

# criar função:
def Kayllane(name):
    print("Meu nome é", name)
# chamar a função:
Kayllane("Kayllane")
Kayllane("Kayh")
Kayllane("Kaka")

# o exercicio acima serviu para resumir a que está embaixo:
def Kayllane():
    name = "Kayllane"
    name2 = "Kayh"
    name3 = "Kaka"
    print("Meu nome é", name)
    print("Meu nome é", name2)
    print("Meu nome é", name3)


# exemplo:
def soma():
    n = int(input("Digite um número:\n"))
    n1 = int(input("Digite outro número:\n"))
    print("A soma é:", n+n1)
soma()
soma()
soma()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exercícios 01: Crie uma tupla chamada `frutas` com pelo menos 5 frutas diferentes. Em seguida, acesse e imprima o terceiro elemento da tupla.
tuple = ("abacaxi","laranja","uva","kiwi", "limão")
frutas = tuple
print(frutas[2])
#outra forma: 
tuple = ("abacaxi","laranja","uva","kiwi", "limão")
index = tuple
print(index[2])

# Exercícios 02: Crie uma tupla chamada numeros com alguns números inteiros. Em seguida, converta essa tupla em uma lista e imprima a lista resultante.
numeros = (1,2,3,4,5)
lista = list(numeros)
print(numeros)

# Exercícios 03: Crie uma tupla chamada `meses` com os nomes dos meses do ano até Setembro. Use um loop `for` para imprimir cada mês em uma linha separada.
tuple = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro")
meses = tuple
for meses in tuple:
    print(meses)
# outra forma: 
meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro")
for i in meses:
    print(i) #i de index

# Exercícios 04: Crie uma lista chamada `notas` com algumas notas de alunos. Em seguida, converta essa lista em uma tupla e imprima a tupla resultante.
notas = [10,9,8,7,6]
tuple = list(notas)
print(tuple)

# Exercícios 05: Crie uma lista chamada `ponto` que represente as coordenadas (x, y) de um ponto. Em seguida, desempacote os elementos da lista em duas variáveis separadas (x e y) e imprima os valores.
ponto = (10,20)
x,y = ponto
print("Coordenada x", x)
print("Coordenada y", y)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exemplo de claculadora
def calculadora():
    x = float(input("Digite o primeiro numero:\n"))
    y = float(input("Digite o primeiro numero:\n"))
    print(x*y)
    print(x+y)
    print(x/y)
    print(x-y)
calculadora ()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Exercício 01: DESAFIO CALCULADORA: 
# OPÇÕES DE OPERAÇÃO
# CONDICIONAIS 
# VARIAVEIS 
# SINAIS DE COMPARAÇÃO (==)  

print(input("Digite a operação desejada:\n"))
def soma():
    x = int(input("Digite o primeiro numero:\n"))
    y = int(input("Digite o segundo numero:\n")) 
    print(x+y)
    if  x == y:
        print("Os números escolhidos são iguais")
    else:
        print("Os números escolhidos não são iguais")
soma()

print(input("Digite a operação desejada:\n"))
def divisão():
    x = int(input("Digite o primeiro numero:\n"))
    y = int(input("Digite o segundo numero:\n")) 
    print(x/y)
    if  x != y:
        print("O resultado não é o número 1")
    else:
        print("O resultado dessa divisão é o número 1")
divisão()

print(input("Digite a operação desejada:\n"))
def multiplicação():
    x = int(input("Digite o primeiro numero:\n"))
    y = int(input("Digite o segundo numero:\n")) 
    print(x*y)
    if  x == y:
        print("O resultado possui uma raíz quadrada")
    else:
        print("O resultado não possui uma raíz quadrada")
multiplicação()

print(input("Digite a operação desejada:\n"))
def subtração():
    x = float(input("Digite o primeiro numero:\n"))
    y = float(input("Digite o segundo numero:\n")) 
    print(x-y)
    if  y == 1:
        print("O resultado é um número anterior do número escolhido para x")
    else:
        print("O resultado é qualquer número, mas nunca o anterior escolhido para x")
subtração()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Seja bem vindo ao Mcdonalds!!! Faça seu pedido digitando a opção desejada:\n (1) - Big Mc\n (2) - Mclanche Feliz\n (3) - Quarteirão")
def Lanche():
    escolha = int(input("Digite o número do lanche desejado:\n"))

    if  escolha == 1:
        print("Seu pedido foi um Big Mc + batatas\n") 

    elif escolha == 2:
        print("Seu pedido foi um Mclanche Feliz + batatas\n")

    else:
        print("Seu pedido foi um Quarteirão + batatas\n")
Lanche()

print("Foi uma ótima escolha de lanche, agora faça seu pedido de bebida:\n (1) - Coca-cola\n (2) - Suco\n (3) - Água\n")
def Bebida():
    escolha01 = int(input("Digite o número da bebida desejada:\n"))

    if  escolha01 == 1:
        print("Seu pedido foi um refrigerante") 
        print(input("Digite qual refrigerante você deseja"))

    elif escolha01 == 2:
        print("Seu pedido foi Suco")
        print(input("Digite qual sabor você deseja:\n"))

    else:
        print("Seu pedido foi água, bem saudável! foi ótima escolha\n")
Bebida()

print("Oba, você já escolheu o lanche e a bebida, mas para finalizar que tal um docinho? Digite o doce desejado podendo ser: Sorvete ou Tortinha\n")
def Sobremesa():
    print(input("Digite qual das duas sobremesas você quer?"))
    print("Uau, ótima escolha!") 
    print(input("Agora digite qual sabor você quer"))
    print("pedido finalizado, aguarde cerca de 30min, muito obrigado")
Sobremesa()
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

#Exercício 01: Crie um dicionário que represente um dicionário de sinônimos. Em seguida, peça ao usuário para digitar uma palavra e, se a palavra estiver no dicionário, mostre o seu sinônimo.
dicionario = {'cair': 'queda', 'morrer': "perdeu a vida", 'longo': 'comprido'}
palavra = (input("Digite uma palavra desse dicionário\n"))
if palavra in dicionario:
   print("O sinônimo é:", dicionario [palavra])
else:
   print("Essa palavra não existe nesse dicionário")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

#AULA 10
#funções com loop for
# usar += significa x = x + y: soma + soma = algum numero

# Exercício 1: Escreva uma função que calcule a soma dos números de 1 a N, onde N é um número inteiro dado. 
print("A soma de 1 até n é:")
def soma(N):
    soma = 0 
    for i in range(1,N+1):
        soma = soma + i 
    print(soma)
soma(2)

# Exercício 2: Escreva uma função que conte quantas vezes uma letra específica aparece em uma palavra.
def contar_letra(palavra,letra):
    contador = 0 
    for char in palavra:
        if char == letra:
           contador += 1
    print(f'tem essa quantidade de {letra}:', contador)
achar = contar_letra('aula','a')

#Exercício 3: Escreva uma função que calcule o fatorial de um número inteiro não negativo N.
#5! = 4x3x2x1 é o produto da multiplicação dos numeros anteriores ao fatorial 

N = int(input('fatorial:'))
resultado = 1
count = 1

while count <=N:
      resultado *= count #multiplicando o resultado 
      count +=1
print(resultado)
 
#Exercício 4: Crie um Dicionário, adicione elementos ao dicionário e os mostre na tela.

dict = {}
dict ['chave 01'] = 'valor01'
dict ['chave 02'] = 'valor02'
dict ['chave 03'] = 'valor03'
dict ['chave 04'] = 'valor04'
dict ['chave 05'] = 'valor05'
dict ['chave 06'] = 'valor06'

print(dict)

#Exercício 5: Utilizando Dicionários, que peça para o usuário inserir o nome de três produtos 

produtos = {}
for i in range(3):
    produto = input("Digite nome do produto:\n")
    preco = input(float("Digite o preço do produto:\n"))
    produtos[produto] = preco 

print('Lista de produtos:')
for produto, preco in produtos.items():
    print('f{produto}: R$ {preco: .2f}')  #2f significa 2 casas depois do float 

