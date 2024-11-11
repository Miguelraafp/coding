from time import sleep as slp
opçoes = 0
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
while opçoes != 4:
    escolhas = print("\n [1] Somar \n [2] Multiplicar \n [3] Subtrair \n [4] Sair \n [5] Novos números: ")
    opçoes = int(input("Qual opção você deseja? "))
    slp(0.4)
    if opçoes == 1:
        print(f"{n1}+{n2}={n1+n2}")
    elif opçoes == 2:
        print(f"{n1} x {n2} = {n1*n2}")
    elif opçoes == 3:
        print(f"{n1} - {n2} = {n1-n2}")
    elif opçoes == 5:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite um número: "))
    slp(0.4)
print("Você saiu do programa!")