from random import *

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[33mO dado não corresponde a um número inteiro')
            continue
        except KeyboardInterrupt:
            print('\033[31m\nA leitura de dados foi interrompida pelo usuário')
            return 0
        
        else:
            return n

print('\033[35m==' * 15)
print("\033[33m{:^30}".format('GERANDO SENHAS'))
print("\033[35m==" * 15)

especiais = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
maiúsculas = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
minusculas = "abcdefghijklmnopqrstuwxyz"
números = "1234567890"


senhas = leiaInt('\033[32mQuantas senhas deseja gerar? ')
dígitos = leiaInt('Quantos dígitos tera na senha? ')
while dígitos <= 7:
    dígitos = leiaInt("\033[33mA quantidade minima de Caracteres é 8: ")

M = leiaInt('\033[32mQuantas maiúsculas terá na senha? ')
m = leiaInt('Quantas minúsculas? ')
c = leiaInt('Quantos caracteres especiais? ')
n = leiaInt('quantos números? ')

print("\033[35m==" * 15)
for pwd in range(0, senhas):
    senha = ""
    cont = 0
    while cont <= dígitos:
        cont += 1
        if M > 0:
            for l in range(0, M):
                cont += 1
                senha += choice(maiúsculas)
                
        if m > 0:
            for l in range(0, m):
                senha += choice(minusculas)
                cont += 1
      
        if c > 0:
            for l in range(0, c):
                senha += choice(especiais)
                cont += 1
        if n > 0:
            for l in range(0, n):
                senha += choice(números)
                cont += 1
     


    print('\033[1;31m{:^30}'.format(senha))
print("\033[35m==" * 15)
print("\033[m", end= "")
