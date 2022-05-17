


# Project one : Par o impar
def even_odd():
    
    # Variables
    playing = True

    print(" vienvenido al juego de Par o Impar ".center(80, "#"))
    print("#" * 80)
    while playing == True:
        try:
            num = int(input("Piensa en un número entero entre 1 y 1000:\n"))
            if num > 0 and num < 1000:
                if num % 2 == 0:
                    print(f"¡El número {num} Es un número par! ", end="")
                else:
                    print(f"¡El número {num} Es un número impar! ", end="")

                if input("Quieres añadir otro? (tipe s o n): ").lower() == "n":
                    playing = False
        except:
            print("Los datos ingresados no son válidos intente de nuevo....")

    print(" Hasta luego ".center(80, "#"))
    print("#" * 80)

def palindromo():

    print(" vienvenido al juego de palíndromo ".center(80, "#"))
    print("#" * 80)
    nombres = input("Ingrese palabras separadas por comas: ").split(", ")
    print(nombres)
    for nombre in nombres:
        if nombre == nombre[::-1]:
            print(f"{nombre} es una palabra palíndromo")
        else:
            print(f"{nombre} no es una palabra palíndromo")

