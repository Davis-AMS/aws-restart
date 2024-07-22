nombre = input("Por favor, ingresa tu nombre: ")
temperatura = float(input("Por favor, ingresa una temperatura en grados Celsius: "))

if temperatura <= 0:
    print("El agua está congelada. No se puede beber.")
elif temperatura >= 100:
    print("El agua está hirviendo. No se puede beber.")
else:
    print("El agua está en un estado adecuado para beber.")





