from time import sleep
resp = 'S'
opcoes = [1, 2, 3]

while resp == 'S':
    print("[1] Refrigerantes\n[2] Hamburguer\n[3] Hot-Dog")
    opcao = int(input("Qual opção? [1], [2], [3]: "))
    if opcao not in opcoes:
        print("Não temos essa opção. Tente novamente! ")
    #sleep(0.5)
    if opcao == 1:
        print("\tCoca-Cola 1L\tPepsi 1L\tGuaraná 1L")
        print("\tR$7.50\t     \tR$7.50  \tR$7.50")
    elif opcao == 2:
        print("\t\tCangaceiro\tXtudo\tXEgg\tNormal")
        print("\t\tR$17.00\t\tR$28.00\tR$20.00\tR$15.00")
    elif opcao == 3:
        print("\t2 Salsichas\t1 Salsicha")
        print("\tR$10.00\t\tR$12.00")
    sleep(0.3)
    resp = str(input("Deseja continuar? [S/N] ")).upper()
print("Volte sempre! ")
