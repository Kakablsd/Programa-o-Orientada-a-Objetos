lista1 = [1,2,3,5,4]

#QUESTÃO 6

print(f"A lista tem {len(lista1)} itens")

#QUESTÃO 7

a = 0
for i in lista1:
    a = a + i

print(a)

#QUESTÃO 8

lista1.sort()
print(lista1)

#QUESTÃO 9

lista1.sort(reverse=True)
print(lista1)

#QUESTÃO 10

verificar = int(input("Digite um número para verificar se o mesmo está na lista: "))

if verificar in lista1:
    print(f"O Número {verificar} está na lista.")

else:
    print(f"O Número {verificar} NÃO está na lista.")
