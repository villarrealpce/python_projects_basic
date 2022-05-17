import string
# crear alfabeto
alphabet = list(string.ascii_lowercase)


direction = input("Escriba 'encode' para encryptar o 'decode' para desencriptar:\n" )
text = input("Escriba su mensaje:\n").lower()
shift = int(input("Escriba el número de cambio:\n"))

# Parte 1. Crear una función llamada 'encrypt'que tome 'text' y 'shift' como entradas

def encrypt(text_input, shift_input):
    # Parte 2. Dentro de la función 'encrypt' cambie cada letra de 'text' hacia adelante  por el valor
    # del 'shift' e imprima el texto encryptado
    ecncrypted_text = []
    for l in text_input:
        index_l = alphabet.index(l) # Ubica idex de cada letra de la palabra
        new_index = index_l+shift_input  # Se registra nuevo index
        if new_index > len(alphabet)-1:
            new_index -= len(alphabet)  # si nevo indice es mayor al idex de la z resta la longitu de alfabeto para posicionarlo en el idex indicado

        letter_encrypted = alphabet[new_index]
        ecncrypted_text.append(letter_encrypted)
    print("".join(map(str, ecncrypted_text)))
   
def caesar(text_input, shift_input, direction_input):
    text_out = []
    if shift_input > len(alphabet)-1:
        shift_input %= len(alphabet)-1
        print(shift_input)
    if direction_input == "decode":
        shift_input *= -1
    for l in text_input:
        index_l = alphabet.index(l)
        new_index = index_l+shift_input
        if new_index > len(alphabet)-1:
            new_index -= len(alphabet)
        elif new_index < 0:
            new_index += len(alphabet)
        text_out.append(alphabet[new_index])
    print("".join(map(str, text_out)))            



caesar(text, shift, direction)


# ubfhydsyfyjeuikdqdqhhqsyedsehjqtubuishyjehvhqdsuiqdjeydutuiqydjunkfuhogkujhqjqtubqxyijehyqtukdfugkuddefhydsyfugkufqhjutuikqijuheytuqkdqjhqluiyqfehubkdyluhieudbqskqbtuiskrhubqunjhqddqvehcqudgkubeiqtkbjeiludbqlytqosecfhudtuublqbehtubqcehobqqcyijqt
# ElprincipitoesunanarracioncortadelescritorfrancesAntoinedeSaintExuperyquetratadelahistoriadeunpequennoprincipequepartedesuasteroideaunatravesiaporeluniversoenlacualdescubrelaextrannaformaenquelosadultosvenlavidaycomprendeelvalordelamorylaamistad