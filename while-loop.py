print("Bienvenido, juguemos a adivinar el número!")
print("Las reglas son simples, yo pienso en un número y tu lo adivinas.")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Adivina un número entre 1 y 10 : ")
    if int(guess) == number:
        print("Adivinaste {}. Si que eres bueno!".format(guess))
        isGuessRight = True
    else:
        print("No acertaste {}. Vuelve a intentarlo.".format(guess))
        print("Recuerda del 1 al 10!")
        
for x in range (0, 11):
    print(x)