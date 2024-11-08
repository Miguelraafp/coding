from random import randint
import emoji, time



numerosort = randint(1, 10)

usuario = 0

while usuario != numerosort:
    usuario = int(input("Qual número você quer? Digite-o abaixo: \n"))
    if usuario < numerosort:
        print("Um pouco mais...")
    elif usuario > numerosort:
        print("Um pouco menos...")
    time.sleep(0.3)
print(emoji.emojize(f"Você acertou!!! O número sorteado foi o {numerosort}. Parabéns!!!! :sunglasses: "))