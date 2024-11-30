lista = []
cont = 0
num = 0
resp = 'S'
while resp == 'S':
    num = int(input("Digite um número: "))
    cont += 1
    lista.append(num)
    resp = str(input("Deseja continuar? [S/N] ")).upper()
media = sum(lista) / cont
print(f"A média dos números digitados é {media:.2f}")
print(f"O maior número foi {max(lista)} e o menor foi {min(lista)}")


