import os
from operator import itemgetter
from art import logo

# Variables
new_user = True
blind_auction = {}
print(logo)

while new_user == True:

    name_user = input("Por favor ingrese el nombre:\n")
    bid_user = float(input("Por favor ingrese el monto:\n"))
    blind_auction[name_user] = bid_user
    new = "quizas"

    while new != "si" and new != "no":
        new = input("Desea agregar una nueva oferta (si - no):\n")
        
        if new == "no":
            new_user = False
        elif new == "si":
            os.system('clear')
    

# Obtener clave con el mayor valor

max_value = max(blind_auction.items(), key=itemgetter(1))

print(f"El ganador es {max_value[0]} con {max_value[1]} Dólares")
