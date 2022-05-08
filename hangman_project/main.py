'''
Identificación del proyecto:
Programa para simular el juego del Hombre Ahorcado (Hangman) 
Curso de Python Bootcamp  "100 Days of Python Pledge" 
dictado por Dr Angela Yu - Día 07 - Principiante
'''
# Importaciones
import os
import random
import hangman_word_list as hmwl
import hangman_image as hmi

# Parte # 1 Generar una palabra aleatoria y convertirla en minúsculas
# La palabra proviene de listado en archivo  hangman_word_list.py
word = random.choice(hmwl.word_list).lower()
# ---------------------  FIN PARTE 1  --------------------------------------

# Parte # 2 Generar lineas para sustituir palabra aleatoria
solution = ""
for l in word:
    if l.isalpha():
        solution += "_"
    elif not l.isalpha():
        solution += " " 
# Parte 2.1. Se inicializan la variable to_discover indica el número de letras a 
# descubrir 
to_discover = solution.count("_")
# Parte 2.2. Se limpia la pantalla y se inicia la parte visual
os.system('clear')
'''
print(hmi.hangman_logo[0])
# print("*"*80)
print("Bienvenidos a Hangman Game".center(80,"*"))
#print("*"*80)
print("Adivina la palabra o la frase".center(80))
print()
print(solution.center(80))
print()'''

# ---------------------  FIN PARTE 2  --------------------------------------

# Parte # 3 Generar lista de gráfica ahorcadoarchivo hangman_image.py
live = 8  # Setea número de vidas
# ---------------------  FIN PARTE 3   --------------------------------------
lts = []
# Parte # 4. Pedir por teclado una letra.
while to_discover > 0 and live > 0:
    os.system('clear')

    print(hmi.hangman_logo[0])
    #print("*"*80)
    print("  Bienvenidos a Hangman Game  ".center(80,"*"))
    #print("*"*80)
    print("  Adivina la palabra o la frase  ".center(80))
    
    print()
    print(solution.center(80))
   
    
    print(hmi.hangman_image[live])
    print()
    print("Letras utilizadas:")
    print(lts)
    print()
    letter = input("Escriba una letra: ")

    # ---------------------  FIN PARTE 4   --------------------------------------

    # Parte # 5. Verificar si la letra está en la palabra
    lts.append(letter)

    if letter in word:
        # 5.1. remplazar la letra en su posición
        l= list(solution)
        for pos,char in enumerate(word):
            if(char == letter):
                l[pos] = char

        solution = "".join(l)
        to_discover = solution.count("_")
       

    else:
        live -= 1
        
# Parte 6 Declarar resultado del Juego

os.system('clear')
if live > 0:
    
    print(hmi.hangman_gameover[0])
else:
   print(hmi.hangman_gameover[1])