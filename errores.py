try:
    numero1 = int(input("Escribe el primer número: "))
    numero2 = int(input("Escribe el segundo número: "))
    resultado = numero1 / numero2
    print(f"El resultado es: {resultado}")
except ValueError:
    print("¡Error! Debes escribir números, no letras.")
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")