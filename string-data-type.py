

# Para denotar que se trata de un string utilizamos
# " "
# o
# ' '
# Con la comilla que abro debo cerrar

myString = "Hola"

print(f"El valor de mi variable es {myString} y su tipo es {type(myString)}")


# Operador
# NO puedo hacer directamente operaciones aritméticas

# Concateción
# Unión de dos o más strings

nombre = "David "
apellido = "Moraga"

nombre_completo = nombre + " " +  apellido # Es concatenación

print("El nombre completo es: ", nombre_completo)

### Función de entrada por teclado
# input()
# frena el programa y espera que el usuario ingrese algo por teclado
# por defecto el valor que se recibe es de tipo string

nombre = input("Ingresa el nombre: ")

apellido = input("Ingresa tu apellido: ")

nombre_completo = nombre + " " + apellido

print(f"Hola, tu nombre es: {nombre_completo}")


# CONVERSIÓN DE TIPOS DE VARIABLE
# CASTING o CASTEO

# Puedo convertir un string a int o float así

variable = "2"
numero_convertido = int(variable)

print(f"La variable era de tipo {type(variable)} y ahora es {type(numero_convertido)}")


"""
Conversiones

int()
float()
complex()
str()

"""

# Voy a sumar dos números
# Si no convierto lo que recibo en input será string
# convierto la entrada de input a int
num = int(input("Ingresa un número: ")) # 5
num2 = int(input("Ingresa otro número: ")) # 2

# al ser strings se concatenarán (unen)
resultado = num + num2

print(f"La suma de {num} y {num2} es {resultado}")


print(f"Tu nombre es: {nombre}")
