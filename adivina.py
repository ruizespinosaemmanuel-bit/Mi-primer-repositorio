secreto = 5000
intento = 1000
while intento != secreto:
    intento = int(input("Adivina el número secreto: "))
    if intento < secreto:
        print("Demasiado bajo, intenta de nuevo.")
    elif intento > secreto:
        print("Demasiado alto, intenta de nuevo.")