# python_projects_basic
Repositorio para la concentración de pequeños proyectos en python

### Primer Proyecto Hangman Game
1. proyecto de categoría básico **The Hangman game**
* Uso de Listas
* Uso de Variables
* Uso de loop while
* Uso de condicional if
2. Se ajusto para validar palabras y frases. ('La noche esta tan bella') es válido
3. Se mantiene el criterio de palabras y frases en minúsculas ***lower case letters***
### Segundo Proyecto caesar cipher
1. proyecto de categoría básico **caesar cipher**
* Uso de funciones sin retorno
* Uso de entrada de datos por teclado
* Uso de condicional if, elif, else
* Uso de listas, list.append
* Uso de método str.join()
* Uso de  funcióm map()
2. Ajustado para reconocer valores de shift mayores a 25
3. Se puede utilizar para cualquier alfabeto pendiente commit con modificación de la linea 29
### Tercer Proyecto blind_auction
1. proyecto de categoría básico **blind auction**
* Uso de diccionarios
* bucle while
* importación de módulos uso de operator.itemgetter
* Uso de función max(int, key)
2. Modificado para limitar la entrada para nueva oferta a las palabras "si" y "no"
3. se eliminó la función para buscar el valor mayor sustituyendola por la siguiente expresión
```python
max_value = max(blind_auction.items(), key=itemgetter(1))
print(f"El ganador es {max_value[0]} con {max_value[1]} Dólares")
```
