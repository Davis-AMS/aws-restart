def verificar_voto(edad, nombre, tiene_identificacion):
    """
    Verifica si una persona es apta para votar.

    Parámetros:
      edad: La edad de la persona.
      nombre: El nombre de la persona.
      tiene_identificacion: True si la persona tiene una identificación válida, False en caso contrario.

    Retorno:
      Un mensaje indicando si la persona es apta para votar o no.
    """
    if edad < 18:
        return f"{nombre} no es apto para votar por ser menor de edad."
    if tiene_identificacion:
        return f"{nombre} es apto para votar."
    return f"{nombre} no es apto para votar por falta de identificación."

# Ejemplo de uso
nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))
tiene_identificacion = input("¿La persona tiene una identificación válida? (sí/no): ").strip().lower() == "sí"

print(verificar_voto(edad, nombre, tiene_identificacion))
