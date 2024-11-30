

lista = []

num = 0
while num < 10:
    num = int(input("Digite um número: "))
    lista.append(num)

print(f"O maior número dessa lista é {max(lista)} e o menor é {min(lista)}")

